"""Ports: what the use case needs from the outside world."""

from typing import Protocol

from stocknews.domain.models import Article


class PriceSource(Protocol):
    """Gives the daily closing prices of a stock."""

    def get_stock_prices(self, symbol: str) -> tuple[float, float]:
        """Return (day before close, yesterday close) of the symbol."""
        ...


class NewsSource(Protocol):
    """Gives the latest news about a company."""

    def get_news(self, company: str, count: int) -> list[Article]:
        """Return at most count articles about the company, newest first."""
        ...


class Notifier(Protocol):
    """Delivers a message to the investor."""

    def send_message(self, text: str) -> None:
        """Deliver one message."""
        ...
