# Wikipedia Game Improvement Proposal

Author: Carlos Garcia - Working Solo

Peer Reviewer: Peter Smith

## Improvements

As of now the WikipediaGame uses a breadth-first search for all the hyperlinks of each page, and goes from the given start page and finishes when it reaches the target page. The Improvement I propose is:


### Deque (Double-ended queue) Two Way Search
When working aider an improvement it suggested that I think would work well, that being a double ended queue from a module called collections. Removing elements from the front of a list is slow to say the least, whereas it's quicker for a deque or double ended queue. This is because adding or removing elements from the front of a deque is a fast operation with popping of elements, whereas removing elements from the front of a list is slow and can significantly slow down the algorithm if the list is long. Creating two sets to keep track of the discovered pages in both directions to find a common page that they share.
### Parallel Processing
Here it also preforms the searches as the same time but much quicker using threading. Both threads are not alternating rather they are doing it at the same time with it using the double ended deque two way search. 


## Pseudo-code for my modification
```
# Pseudocode for Deque Two-Way Search with Parallel Processing

# Import necessary libraries
import threading
from collections import deque

# Initialize two deques for forward and backward search
forward_deque = deque([start_page])
backward_deque = deque([end_page])

# Initialize sets to keep track of visited pages in both directions
forward_visited = set([start_page])
backward_visited = set([end_page])

# Define a function to fetch and process a page
def fetch_and_process_page(page_url, direction):
    # Fetch the page
    # Extract the links
    # Process the links based on the direction of the search
    pass

# Define a function to perform the search in one direction
def search_in_direction(direction_deque, visited_set, opposite_visited_set, direction):
    while direction_deque:
        # Pop a page from the deque
        # Fetch and process the page in a new thread
        # Check if any of the links are in the opposite visited set
        # If so, the search is complete
        # Otherwise, add the links to the deque and the visited set
        pass

# Start two threads to perform the search in both directions
threading.Thread(target=search_in_direction, args=(forward_deque, forward_visited, backward_visited, 'forward')).start()
threading.Thread(target=search_in_direction, args=(backward_deque, backward_visited, forward_visited, 'backward')).start()

# Wait for both threads to finish
# Return the path from the start page to the end page
```

### Library Added 
```
from collections import deque
import threading
```

## Milestones
Milestone 1: Setup the development environment with the necessary libraries and dependecies need (3/28)
Milestone 2: Designing the Deque Two Way Search - Based on the pseudocode, design the detailed algorithm for the two-way search. This includes deciding how to split the search into two directions, how to manage the deques and visited sets, and how to combine the results from the two directions. Verification: Have a written plan for the two-way search algorithm, including how to manage the deques and visited sets, and how to combine the results from the two directions. (4/3)
Milestone 3: Implement the search_in_direction Function - Implement the function to perform the search in one direction. This function should be able to pop a page from the deque, fetch and process the page in a new thread, check if any of the links are in the opposite visited set, and if not, add the links to the deque and the visited set. This will involve using the threading library to create and manage the threads. Verification: Have a working search_in_direction function that can perform the search in one direction, using multithreading to fetch and process pages. (4/10)
Milestone 4: Implement the Parallel Processing - Implement the logic to start two threads and perform the search in both directions simultaneously. This includes managing the threads and ensuring that they can run and complete independently. Verification: Have a working implementation that can perform the search in both directions simultaneously, using multithreading. (4/24)
Milestone 5: Testing and Documentation - Test the implementation with different start and end pages to ensure that it works correctly. Based on that optimize any inconsistencies that may pop up and problems that may arise when debugging. 
