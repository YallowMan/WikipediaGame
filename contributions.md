# Contributions
This was a solo project, so I developed and worked on my own.

## AI
I used both Aider and ChatGPT for pieces of code generation and debugging (as advised in the project). 

## 
The program can fairly quickly find a connection between two pages compared to the original version of the algorithm, but at first glance may not seem like its all too better. It can find pages that are close to each other in incredibly fast times, but tends to have many discovered pages in return. All in all, it was a different kind of experience when it came to working on this algorithm especially when working with Aider and ChatGPT, but more specifically Aider. I never have worked with an Ai pair program before and I will say that it was a good learning experience as sometimes it would help cleanup my code and provide a similar suggestion to what I had created that made more sense when directly looking at it. My method for the bidirectional search changed from the start of the proposal as I thought a better solution for going backwards would be to use backlinks using the Wikipedia API.

## How to Test
### Sample Input 1 
- Starting URL: `https://en.wikipedia.org/wiki/Michelangelo`
- Finish URL: `https://en.wikipedia.org/wiki/The_Godfather`
My Algorithm:
`
Found meeting point: https://en.wikipedia.org/wiki/Italians
Search took 4.945229768753052 seconds.
Discovered pages: 3727
`

Previous Algorithm:
`
Found finish page: [https://en.wikipedia.org/wiki/Italians](https://en.wikipedia.org/wiki/The_Godfather)
Search took 102.03139114379883 seconds.
Discovered pages: 28677
`
### Sample Input 2
- Starting URL: ``
- Finish URL: ``
My Algorithm:
`

`

Previous Algorithm:
`

`
