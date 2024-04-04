import time
import requests
from bs4 import BeautifulSoup
import re

TIMEOUT = 1800  # time limit in seconds for the search

def get_links(page_url):
    print(f"Fetching page: {page_url}")
    response = requests.get(page_url)
    print(f"Finished fetching page: {page_url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    from urllib.parse import urljoin
    all_links = [urljoin(page_url, a['href']) for a in soup.find_all('a', href=True) if '#' not in a['href']]
    # print(f"All links found: {all_links}")
    links = [link for link in all_links if re.match(r'^https://en\.wikipedia\.org/wiki/[^:]*$', link) and '#' not in link]
    print(f"Found {len(links)} links on page: {page_url}")
    return links

from collections import deque

def find_path(start_page, finish_page):
    forward_queue = deque([(start_page, [start_page])])
    backward_queue = deque([(finish_page, [finish_page])])
    forward_visited = {start_page}
    backward_visited = {finish_page}
    logs = []

    # bidirectional search
    start_time = time.time()
    elapsed_time = time.time() - start_time
    while forward_queue and backward_queue and elapsed_time < TIMEOUT:
        forward_vertex, forward_path = forward_queue.popleft()
        backward_vertex, backward_path = backward_queue.popleft()
        for next in set(get_links(forward_vertex)) - forward_visited:
            if next in backward_visited:
                log = f"Found meeting point: {next}"
                print(log)
                logs.append(log)
                logs.append(f"Search took {elapsed_time} seconds.")
                print(f"Search took {elapsed_time} seconds.")
                logs.append(f"Discovered pages: {len(forward_visited) + len(backward_visited)}")
                return forward_path + backward_path[::-1], logs, elapsed_time, len(forward_visited) + len(backward_visited)
            else:
                log = f"Adding link to forward queue: {next}"
                print(log)
                logs.append(log)
                forward_visited.add(next)
                forward_queue.append((next, forward_path + [next]))
        for next in set(get_links(backward_vertex)) - backward_visited:
            if next in forward_visited:
                log = f"Found meeting point: {next}"
                print(log)
                logs.append(log)
                logs.append(f"Search took {elapsed_time} seconds.")
                print(f"Search took {elapsed_time} seconds.")
                logs.append(f"Discovered pages: {len(forward_visited) + len(backward_visited)}")
                return forward_path + backward_path[::-1], logs, elapsed_time, len(forward_visited) + len(backward_visited)
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
