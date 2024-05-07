# WikipediaGame

## Description
This project is an optimization and alteration of a project started by [Alexander Kurz](https://github.com/alexhkurz) of his Wikipedia Search game with his orignal source code being [https://github.com/alexhkurz/WikipediaGame](https://github.com/alexhkurz/WikipediaGame). The original game consisting of a breadth-first search extracting any and all hyperlinks on each page that starts from a given starting input page and finishing when it reaches the target page. All links that are traversed through are sent to a queue in which we use said queue to find the finishing page, this can find the shortest path, but is able to be improved upon from a time standpoint. With my optimization I altered the algorithm to act as a bidirectional search rather than a breadth-first search, where it maintains two queues of pages, one starts from the start page and moves forward through the links, and the other starting from the given finishing page and moving backwards using backlinks with the wikipedia api. What is also implemented is a multiprocessing pool that fetches and process multiple pages in parallel, the search will stop when a page is found in both queues which will act as the meeting point and this will indicate there has been a path found from the start page to the finish page.
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

(For development one may want to use `watchmedo auto-restart -d . -p '*.py' -- python server.py`.)

Play the game on [`localhost:5000`](http://127.0.0.1:5000/) (this link will only work after you started the server on your machine (watch the console in case the port number changed to eg `5001`)).

## Limitations

- The UI works as expected only for chrome-based browsers (Chrome, Brave, ...).
- Only works for wikipedia pages.
- Users are identified by IP adress (no cookies or sessions).
- May have problems on public networks where connection will be reset by peer.

## Parameters

- `RATELIMIT` in `server.py`.
- `TIMEOUT` in `crawler.py`.




