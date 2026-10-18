"""Alpha Vantage client for daily closing prices."""

from stocknews import constants
from stocknews.domain.errors import ApiError
from stocknews.infrastructure import http

## Keys Alpha Vantage uses to report errors and quota limits.
_ERROR_KEYS = ("Error Message", "Note", "Information")


def get_stock_prices(symbol: str, api_key: str) -> tuple[float, float]:
    """Fetch the two latest daily closes of a symbol.

    @param symbol The stock symbol.
    @param api_key The Alpha Vantage key.
    @return (close of the day before, close of the latest day).
    @throws ApiError on an error, a quota message or fewer than two days.
    """
    data = http.get_json(
        constants.STOCK_ENDPOINT,
        {
            "function": constants.STOCK_FUNCTION,
            "symbol": symbol,
            "apikey": api_key,
        },
        constants.HTTP_TIMEOUT_SECONDS,
    )
    for key in _ERROR_KEYS:
        if key in data:
            raise ApiError(f"Alpha Vantage: {data[key]}")
    series = data.get(constants.SERIES_KEY)
    if not isinstance(series, dict) or len(series) < 2:
        raise ApiError("Alpha Vantage returned fewer than two days of prices")
    latest, previous = sorted(series, reverse=True)[:2]
    try:
        return (
            float(series[previous][constants.CLOSE_KEY]),
            float(series[latest][constants.CLOSE_KEY]),
        )
    except (KeyError, TypeError, ValueError) as error:
        raise ApiError("Alpha Vantage returned an unreadable price") from error


class AlphaVantagePrices:
    """PriceSource backed by Alpha Vantage."""

    def __init__(self, api_key: str) -> None:
        """Keep the API key.

        @param api_key The Alpha Vantage key.
        """
        self._api_key = api_key

    def get_stock_prices(self, symbol: str) -> tuple[float, float]:
        """Return (day before close, yesterday close) of the symbol."""
        return get_stock_prices(symbol, self._api_key)
