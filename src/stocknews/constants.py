"""Constants of the stock news program.

All values that the assignment lets the learner change are here, so that
nothing is written twice.
"""

## The stock symbol to watch.
STOCK = "TSLA"

## The company name used to search for news.
COMPANY_NAME = "Tesla Inc"

## The price change in percent (up or down) that triggers an alert.
THRESHOLD_PERCENT = 5.0

## The number of news articles to send with an alert.
NEWS_COUNT = 3

## Alpha Vantage endpoint and the function that returns daily prices.
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_FUNCTION = "TIME_SERIES_DAILY"

## NewsAPI endpoint that searches all articles.
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## The key of the closing price in an Alpha Vantage daily record.
CLOSE_KEY = "4. close"

## The key of the daily records in an Alpha Vantage response.
SERIES_KEY = "Time Series (Daily)"

## Seconds to wait for an API answer before giving up.
HTTP_TIMEOUT_SECONDS = 20

## Environment variable names read by the program.
ENV_STOCK_API_KEY = "APLHA_VANTAGE_API_KEY"
ENV_NEWS_API_KEY = "NEWAPI_KEY"
ENV_PHONE_NUMBER = "STOCKNEWS_PHONE"

## Seconds pywhatkit waits for the browser before it sends the message.
SEND_WAIT_SECONDS = 15
