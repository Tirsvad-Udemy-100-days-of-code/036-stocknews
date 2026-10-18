"""Use case UC-001: receive a stock news alert."""

import logging

from stocknews.application.messages import format_message
from stocknews.application.ports import NewsSource, Notifier, PriceSource
from stocknews.domain.models import PriceChange
from stocknews.domain.rules import calculate_change, is_significant

_log = logging.getLogger(__name__)


def check_stock(
    prices: PriceSource,
    news: NewsSource,
    notifier: Notifier,
    symbol: str,
    company: str,
    threshold: float,
    count: int,
) -> list[str]:
    """Send the latest news when the stock moved by the threshold.

    @param prices Source of the closing prices.
    @param news Source of the news articles.
    @param notifier Receiver of the messages.
    @param symbol The stock symbol.
    @param company The company name used to search for news.
    @param threshold The change in percent that triggers an alert.
    @param count The number of articles to send.
    @return The messages sent; empty when the change is below the threshold.
    """
    previous_close, latest_close = prices.get_stock_prices(symbol)
    percent = calculate_change(previous_close, latest_close)
    if not is_significant(percent, threshold):
        _log.info("%s moved %.2f%%, below the threshold", symbol, percent)
        return []
    change = PriceChange(symbol, previous_close, latest_close, percent)
    messages = [format_message(change, a) for a in news.get_news(company, count)]
    for message in messages:
        notifier.send_message(message)
    return messages
