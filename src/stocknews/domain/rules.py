"""Business rules for price changes."""

from stocknews.domain.errors import InvalidPriceError

_PERCENT = 100.0


def calculate_change(previous_close: float, latest_close: float) -> float:
    """Calculate the signed change in percent between two closes.

    @param previous_close The close of the day before; must be positive.
    @param latest_close The close of the latest day; must not be negative.
    @return (latest - previous) / previous * 100.
    @throws InvalidPriceError when a price is not usable.
    """
    if previous_close <= 0 or latest_close < 0:
        raise InvalidPriceError("closing prices must be positive")
    return (latest_close - previous_close) / previous_close * _PERCENT


def is_significant(percent: float, threshold: float) -> bool:
    """Tell whether a change, up or down, reaches the threshold.

    @param percent The signed change in percent.
    @param threshold The threshold in percent.
    @return True when abs(percent) >= threshold.
    """
    return abs(percent) >= threshold
