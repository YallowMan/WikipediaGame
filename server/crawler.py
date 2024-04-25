import time
import requests
from bs4 import BeautifulSoup
import re

TIMEOUT = 1800  # time limit in seconds for the search

def get_links(page_url):
    """
    This function takes a Wikipedia page URL as input and returns a list of all Wikipedia pages that it links to.
    It sends a GET request to the given URL, parses the HTML response to extract all outbound links,
    and filters out any links that do not lead to other Wikipedia pages.
    """

    print(f"Fetching page: {page_url}")
    for _ in range(5):  # try 5 times
        try:
            # Send a GET request to the page URL
            response = requests.get(page_url)
            print(f"Finished fetching page: {page_url}")
            break
        except requests.exceptions.RequestException as e:
            # If the request fails, print an error message and try again
            print(f"Request failed with error {e}, retrying...")
    else:  # if we exhausted all retries and still failed, re-raise the last exception
        raise

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all outbound links from the HTML
    # We use the urljoin function to construct the full URL for each link
    from urllib.parse import urljoin
    all_links = [urljoin(page_url, a['href']) for a in soup.find_all('a', href=True) if '#' not in a['href']]

    # Filter out any links that do not lead to other Wikipedia pages
    links = [link for link in all_links if re.match(r'^https://en\.wikipedia\.org/wiki/[^:]*$', link) and '#' not in link]

    print(f"Found {len(links)} links on page: {page_url}")
    return links

def get_inbound_links(page_url):
    """
    This function takes a Wikipedia page URL as input and returns a list of all Wikipedia pages that link to it.
    Uses the Wikipedia API to get the list of backlinks for the given page.
    """

    # Extract the page title from the URL
    page_title = page_url.split('/')[-1]

    # Set up the API request
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "backlinks",
        "bltitle": page_title,
        "bllimit": "max"
    }

    # Send the API request and get the response
    response = requests.get(api_url, params=params)
    response_data = response.json()

    # Extract the inbound links from the response data
    # The 'backlinks' field in the response contains a list of pages that link to the given page.
    # We extract the title of each page and construct the full URL by appending it to the Wikipedia base URL.
    inbound_links = ["https://en.wikipedia.org/wiki/" + page['title'] for page in response_data['query']['backlinks']]

    return inbound_links

from multiprocessing import Pool
from collections import deque

def find_path(start_page, finish_page):
    forward_queue = deque([(start_page, [start_page])])
    backward_queue = deque([(finish_page, [finish_page])])
    with Pool(processes=4) as pool:  # adjust the number of processes as needed
        forward_visited = {start_page}
        backward_visited = {finish_page}
        logs = []

        # bidirectional search
        start_time = time.time()
        elapsed_time = time.time() - start_time
        while forward_queue and backward_queue and elapsed_time < TIMEOUT:
            forward_vertex, forward_path = forward_queue.popleft()
            backward_vertex, backward_path = backward_queue.popleft()
            results = pool.map(get_links, [forward_vertex])  # forward search uses outbound links
            for next in set(results[0]) - forward_visited:
                if next in backward_visited:
                    log = f"Found meeting point: {next}"
                    print(log)
                    logs.append(log)
                    logs.append(f"Search took {elapsed_time} seconds.")
                    print(f"Search took {elapsed_time} seconds.")
                    logs.append(f"Discovered pages: {len(forward_visited) + len(backward_visited)}")
                    forward_path.append(next)
                    backward_path.append(next)
                    path = forward_path + backward_path[::-1]
                    full_path = forward_path + backward_path[::-1][1:]
                    print(" -> ".join(full_path))
                    return full_path, logs, elapsed_time, len(forward_visited) + len(backward_visited), full_path
                else:
                    log = f"Adding link to forward queue: {next}"
                    print(log)
                    logs.append(log)
                    forward_visited.add(next)
                    forward_queue.append((next, forward_path + [next]))
            results = pool.map(get_inbound_links, [backward_vertex])  # backward search uses inbound links
            for next in set(results[0]) - backward_visited:
                if next in forward_visited:
                    log = f"Found meeting point: {next}"
                    print(log)
                    logs.append(log)
                    logs.append(f"Search took {elapsed_time} seconds.")
                    print(f"Search took {elapsed_time} seconds.")
                    logs.append(f"Discovered pages: {len(forward_visited) + len(backward_visited)}")
                    full_path = forward_path + backward_path[::-1][1:]
                    print(" -> ".join(full_path))
                    return full_path, logs, elapsed_time, len(forward_visited) + len(backward_visited), full_path
                else:
                    log = f"Adding link to backward queue: {next}"
                    print(log)
                    logs.append(log)
                    backward_visited.add(next)
                    backward_queue.append((next, backward_path + [next]))
            elapsed_time = time.time() - start_time
        logs.append(f"Search took {elapsed_time} seconds.")
        print(f"Search took {elapsed_time} seconds.")
        logs.append(f"Discovered pages: {len(forward_visited) + len(backward_visited)}")
        raise TimeoutErrorWithLogs("Search exceeded time limit.", logs, elapsed_time, len(forward_visited) + len(backward_visited))
class TimeoutErrorWithLogs(Exception):
    def __init__(self, message, logs, time, discovered):
        super().__init__(message)
        self.logs = logs
        self.time = time
        self.discovered = discovered
