# Wikipedia Game Improvement Proposal

Author: Carlos Garcia - Working Solo

Peer Reviewer: Peter Smith

## Improvement

As of now the WikipediaGame uses a breadth-first search for all the hyperlinks of each page, and goes from the given start page and finishes when it reaches the target page. The Improvement I propose is:


### Deque (Double-ended queue) Two Way Search
When working aider an improvement it suggested that I think would work well, that being a double ended queue from a module called collections. Removing elements from the front of a list is slow to say the least, whereas it's quicker for a deque or double ended queue. This is because adding or removing elements from the front of a deque is a fast operation with popping of elements, whereas removing elements from the front of a list is slow and can significantly slow down the algorithm if the list is long. Creating two sets to keep track of the discovered pages in both directions to find a common page that they share.



## Pseudo-code for my modification
```
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
