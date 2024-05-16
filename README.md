# WikipediaGame

## Description
This project is an optimization and alteration of a project started by [Alexander Kurz](https://github.com/alexhkurz) of his Wikipedia Search game with his original source code being [https://github.com/alexhkurz/WikipediaGame](https://github.com/alexhkurz/WikipediaGame). The original game consisting of a breadth-first search extracting any and all hyperlinks on each page that starts from a given starting input page and finishing when it reaches the target page. All links that are traversed through are sent to a queue in which we use said queue to find the finishing page, this can find the shortest path, but is able to be improved upon from a time standpoint. With my optimization I altered the algorithm to act as a bidirectional search rather than a breadth-first search, where it maintains two deques(double-ended queues) of pages, one starts from the start page and moves forward through the links, and the other starting from the given finishing page and moving backwards using backlinks with the Wikipedia API. What is also implemented is a multiprocessing pool that fetches and process multiple pages in parallel, the search will stop when a page is found in both deques which will act as the meeting point and this will indicate there has been a path found from the start page to the finish page. 
## Installation
Prerequisites: Python

```
git clone https://github.com/YallowMan/WikipediaGame.git
cd WikipediaGame/server
source setup.sh
```
To start the server:

```
python server.py
```
If the code above does not start it you may want to use `python3`.

```
python3 server.py

```
Play the game on [`localhost:5000`](http://127.0.0.1:5000/) (this link will only work after you started the server on your machine (watch the console in case the port number changed to eg `5001`)).

## Limitations

- The UI works as expected only for chrome-based browsers (Chrome, Brave, ...).
- Only works for wikipedia pages.
- May have problems on public networks where connection will be reset by peer.

## Parameters

- `RATELIMIT` in `server.py`.
- `TIMEOUT` in `crawler.py`.
  
## Testing 
- Run the installation steps to start the server and then when you are in the game UI enter two Wikipedia links in both the "Start Page URL" and "Finish Page URL" fields.
- When it comes to testing, I used different starting and end pages, some that were bound to have something similar in nature and others not so much. Things like [NASA](https://en.wikipedia.org/wiki/NASA) and [Bill Nye](https://en.wikipedia.org/wiki/Bill_Nye) which were in similar types of fields and then the [Congo River](https://en.wikipedia.org/wiki/Congo_River) and [John Wick](https://en.wikipedia.org/wiki/John_Wick) which don't seem to have much correlation. The further apart they were the longer it would take and it was possible for the algorithm to be less successful when searching. It was fairly quick when finding the mid point that links the path between the two when the pages are more closely related or similar which also provided an accurate result.




