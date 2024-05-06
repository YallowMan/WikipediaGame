# WikipediaGame

## Installation
Prerequisites: Python

```
git clone [https://github.com/alexhkurz/WikipediaGame.git](https://github.com/YallowMan/WikipediaGame.git)
cd WikipediaGame/server
source setup.sh
```

Starting the server:

```
python server.py
```

(For development one may want to use `watchmedo auto-restart -d . -p '*.py' -- python server.py`.)

Play the game on [`localhost:5000`](http://127.0.0.1:5000/) (this link will only work after you started the server on your machine (watch the console in case the port number changed to eg `5001`)).

## Limitations

- The UI works as expected only for chrome-based browsers (Chrome, Brave, ...).
- Only tested for pages that are no further than two hops away. 
- Only works for wikipedia pages.
- Implemented via HTTP requests (no websocket connection between client and server).
- Users are identified by IP adress (no cookies or sessions).
- ...

## Parameters

- `RATELIMIT` in `server.py`.
- `TIMEOUT` in `crawler.py`.

## Further Ideas

- Improve the efficiency of the search.
- Add heuristics for faster search.
- Use LLMs to make better guesses, resulting in faster search.
- ...

## Branches

- `version1` computes the shortest path betwen two wikipedia pages
- `version2` (=`main`) additionally displays all pages visited during the computation
- `dev` will output the pages being visited in real time (under development)



