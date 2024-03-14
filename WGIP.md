# Wikipedia Game Improvement Proposal

Author: Carlos Garcia

## Improvement

As of now the WikipediaGame uses a breadth-first search for all the hyperlinks of each page, and goes from the given start page and finishes when it reaches the target page. The Improvements I propose are:

### Caching
The Wikipedia Game as it sits does not have a way to avoid any redundant searches so a way to fix that would be to implement caching. This would speed up efficiency as well as its able to fetch that info from a directory where the results are stored.By storing the links of each fetched page in a cache, we avoid fetching the same page multiple times. This can reduce the number of requests made to the server, which not only speeds up the script but also reduces the load on the server.

### Deque (Double-ended queue)
When working aider an improvement it suggested that I think would work well, that being a double ended queue from a module called collections. Removing elements from the front of a list is slow to say the least, whereas it's quicker for a deque or double ended queue.  This is because adding or removing elements from the front of a deque is a fast operation with popping of elements, whereas removing elements from the front of a list is slow and can significantly slow down the algorithm if the list is long.


## Pseudo-code for my modification
```
 Create an empty dictionary called link_cache

 Define get_links function with page_url as parameter:
     If page_url is in link_cache:
         Return the value of page_url in link_cache
     Else:
         Fetch the page and parse it to get the links
         Store the links in link_cache with page_url as the key
         Return the links

 Import deque from collections


 Define find_path function with start_page and finish_page as parameters:
     Initialize queue as a deque with (start_page, [start_page], 0) as the only element
     Initialize discovered as an empty set
     Initialize logs as an empty list

     Start timing

     While queue is not empty and elapsed time is less than TIMEOUT:
         Pop (vertex, path, depth) from the front of the queue
         For each link in get_links(vertex) that is not in discovered:
             If link is finish_page:
                 Log the discovery of the finish page
                 Log the elapsed time
                 Log the number of discovered pages
                 Return path + [link], logs, elapsed_time, len(discovered)
             Else:
                 Log the addition of the link to the queue
                 Add link to discovered
                 Append (link, path + [link], depth + 1) to the back of the queue
         Update elapsed time

     Log the elapsed time
     Log the number of discovered pages
     Raise TimeoutErrorWithLogs

```

### Library Added 
```
from collections import deque
```
