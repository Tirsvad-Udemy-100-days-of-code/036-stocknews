"""Errors raised by the stock news program."""


class StockNewsError(Exception):
    """Base class of every error the program raises on purpose."""


class InvalidPriceError(StockNewsError):
    """A closing price cannot be used to calculate a change."""


class ApiError(StockNewsError):
    """An external service failed, answered badly or refused the request."""


class NotificationError(StockNewsError):
    """A message could not be sent to the owner."""


class ConfigError(StockNewsError):
    """A required setting is missing or a required package is not installed."""
