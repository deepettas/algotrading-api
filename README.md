# algotrading-api

## Running the api

### Dependencies

`pip install -r requirements.txt`

### Run

`python start_api.py`

## Running the crawler(s)

`python start_crawler.py [crawler_name] (params)`
`params` are in the form `key:value`. Their parsing is the responsibility of the subsequent crawlers.

For example, you can pass the api key as a parameter (`apikey:asdfasdf`) or wait intervals (`wait_min:1`) or whatever you want.

## Running the ML experiments
