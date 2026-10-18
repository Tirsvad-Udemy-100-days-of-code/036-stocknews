"""Value objects of the stock news domain."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PriceChange:
    """The change of a stock between two daily closes.

    @param symbol The stock symbol.
    @param previous_close The close of the day before.
    @param latest_close The close of the latest day.
    @param percent The signed change in percent.
    """

    symbol: str
    previous_close: float
    latest_close: float
    percent: float


@dataclass(frozen=True, slots=True)
class Article:
    """A news article.

    @param title The headline.
    @param description The brief.
    """

    title: str
    description: str
