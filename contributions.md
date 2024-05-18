# Contributions
- This was a solo project, so I developed and worked on my own.
I altered the following in `server.py`:
- Added a `get_inbound_links` function which takes the Wikipedia page URL finishing page and returns a list of all Wikipedia pages that link to it. It uses the Wikipedia API to get the list of backlinks for the given page.
- Altered the `find_path` function to preform a bidirectional search using two deques to preform the search in both directions simultaneously. The search stopos when a common page is found in both directions and uses a form of threading, where it creates a process pool to fetch the links from multiple pages concurrently.

## Goal
- The goal for this project was to be an improvement to the original WikipediaGame started by Alexander Kurz, by focusing entirely on speed by using a bidrectional search rather than a Breadth-First Search.
- The bidrectional search having two searches in each direction, one using the normal method that goes forward with links and the other using backlinks so that they eventually converge onto each other and give a midpoint and thus a path.
  
## AI
I used both Aider and ChatGPT for pieces of code generation and debugging (as advised in the project). 

## Issue

## Testing
### Sample Input 1 
- Starting URL: `https://en.wikipedia.org/wiki/Michelangelo`
- Finish URL: `https://en.wikipedia.org/wiki/The_Godfather`
  
My Algorithm:
```
Found meeting point: https://en.wikipedia.org/wiki/Italians
Search took 4.945229768753052 seconds.
Discovered pages: 3727
```

Previous Algorithm:
```
Found finish page: https://en.wikipedia.org/wiki/The_Godfather
Search took 102.03139114379883 seconds.
Discovered pages: 28677
```

My Algorithm was able to quickly find it compared to the previous even though these two items are really related and discovered less pages total.

### Sample Input 2
- Starting URL: `https://en.wikipedia.org/wiki/Stardew_Valley`
- Finish URL: `https://en.wikipedia.org/wiki/Alpaca`
  
My Algorithm:
```
Found meeting point: https://en.wikipedia.org/wiki/Andes
Search took 1.391754388809204 seconds.
Discovered pages: 1781
```

Previous Algorithm:
```
Found finish page: https://en.wikipedia.org/wiki/Alpaca
Search took 249.585745096206665 seconds
Discovered pages: 15501 
```

My version of the algorithm significantly improved how quickly the search took overall as well as how many pages needed to be opened, because its not as limiting when using backlinks via the API and didn't limit the paths of legnth 2 like the original.

### Sample Input 3
- Starting URL: `https://en.wikipedia.org/wiki/OLED`
- Finish URL: `https://en.wikipedia.org/wiki/Pi`
  
My Algorithm:
```
Found meeting point: https://en.wikipedia.org/wiki/Frequency
Search took 0.0 seconds.
Discovered pages: 921
```

Previous Algorithm:
```
Found finish page: https://en.wikipedia.org/wiki/Pi
Search took 199.12512159347534 seconds.
Discovered pages: 38013
```

My version of the algorithm would sometimes be too quick to count the search time and would give a flat 0 seconds of time it took for the search. While this does look like an error, it was still able to find a midpoint as well. With a dramatic decrease in discovered pages as well which seems to be the case most of the time.

## Improvement Comparison
- The main purpose of the improvements proposed was to enhance overall speed by integrating backlink fetching via the Wikipedia API to avoid webscraping and speed up the process. 
- The program can fairly quickly find a connection between two pages compared to the original version of the algorithm, but at first glance may not seem like its all too better.
  
## Final Notes
All in all, it was a different kind of experience when it came to working on this algorithm especially when working with Aider and ChatGPT, but more specifically Aider. I never have worked with an Ai pair program before and I will say that it was a good learning experience as sometimes it would help cleanup my code and provide a similar suggestion to what I had created that made more sense when directly looking at it. My method for the bidirectional search changed from the start of the proposal as I thought a better solution for going backwards would be to use backlinks using the Wikipedia API.
