from typing import Any

import pytest

from stocknews import constants
from stocknews.domain.errors import ApiError
from stocknews.infrastructure import alpha_vantage, http


def serve(monkeypatch: pytest.MonkeyPatch, payload: dict[str, Any]) -> list[Any]:
    calls: list[Any] = []

    def fake(url: str, params: dict[str, Any], timeout: float) -> dict[str, Any]:
        calls.append((url, params))
        return payload

    monkeypatch.setattr(http, "get_json", fake)
    return calls


def day(close: str) -> dict[str, str]:
    return {constants.CLOSE_KEY: close}


def test_get_stock_prices_returns_two_latest_closes_oldest_first(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    series = {
        "2026-10-14": day("1.0"),
        "2026-10-16": day("120.5"),
        "2026-10-15": day("100.0"),
    }
    calls = serve(monkeypatch, {constants.SERIES_KEY: series})
    prices = alpha_vantage.AlphaVantagePrices("KEY").get_stock_prices("TSLA")
    assert prices == (100.0, 120.5)
    url, params = calls[0]
    assert url == constants.STOCK_ENDPOINT
    assert params["symbol"] == "TSLA"
    assert params["function"] == constants.STOCK_FUNCTION


@pytest.mark.parametrize("key", ["Error Message", "Note", "Information"])
def test_get_stock_prices_raises_on_error_or_quota_keys(
    monkeypatch: pytest.MonkeyPatch, key: str
) -> None:
    serve(monkeypatch, {key: "limit reached"})
    with pytest.raises(ApiError, match="limit reached"):
        alpha_vantage.get_stock_prices("TSLA", "KEY")


@pytest.mark.parametrize(
    "payload",
    [{}, {constants.SERIES_KEY: {"2026-10-15": day("1")}}, {constants.SERIES_KEY: []}],
)
def test_get_stock_prices_raises_when_fewer_than_two_days(
    monkeypatch: pytest.MonkeyPatch, payload: dict[str, Any]
) -> None:
    serve(monkeypatch, payload)
    with pytest.raises(ApiError, match="fewer than two"):
        alpha_vantage.get_stock_prices("TSLA", "KEY")


def test_get_stock_prices_raises_when_close_is_unreadable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    series = {"2026-10-15": day("x"), "2026-10-16": {}}
    serve(monkeypatch, {constants.SERIES_KEY: series})
    with pytest.raises(ApiError, match="unreadable"):
        alpha_vantage.get_stock_prices("TSLA", "KEY")
