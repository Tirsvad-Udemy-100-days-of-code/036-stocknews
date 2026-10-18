import pytest

from stocknews.application.check_stock import check_stock
from stocknews.domain.errors import ApiError, InvalidPriceError
from stocknews.domain.models import Article


class FakePrices:
    def __init__(self, closes: tuple[float, float]) -> None:
        self.closes = closes

    def get_stock_prices(self, symbol: str) -> tuple[float, float]:
        return self.closes


class FakeNews:
    def __init__(self) -> None:
        self.calls: list[tuple[str, int]] = []

    def get_news(self, company: str, count: int) -> list[Article]:
        self.calls.append((company, count))
        return [Article(f"T{i}", f"D{i}") for i in range(count)]


class FakeNotifier:
    def __init__(self) -> None:
        self.sent: list[str] = []

    def send_message(self, text: str) -> None:
        self.sent.append(text)


class FailingNews:
    def get_news(self, company: str, count: int) -> list[Article]:
        raise ApiError("boom")


def run(closes: tuple[float, float]) -> tuple[list[str], FakeNews, FakeNotifier]:
    news, notifier = FakeNews(), FakeNotifier()
    messages = check_stock(
        FakePrices(closes), news, notifier, "TSLA", "Tesla Inc", 5.0, 3
    )
    return messages, news, notifier


def test_check_stock_sends_one_message_per_article_when_change_is_large() -> None:
    messages, news, notifier = run((100.0, 106.0))
    assert len(messages) == 3
    assert notifier.sent == messages
    assert news.calls == [("Tesla Inc", 3)]
    assert messages[0].startswith("TSLA: ")


def test_check_stock_sends_nothing_when_change_is_small() -> None:
    messages, news, notifier = run((100.0, 101.0))
    assert messages == []
    assert notifier.sent == []
    assert news.calls == []


def test_check_stock_propagates_invalid_price() -> None:
    with pytest.raises(InvalidPriceError):
        run((0.0, 1.0))


def test_check_stock_sends_nothing_when_news_fails() -> None:
    notifier = FakeNotifier()
    with pytest.raises(ApiError):
        check_stock(
            FakePrices((100.0, 110.0)),
            FailingNews(),
            notifier,
            "TSLA",
            "Tesla Inc",
            5.0,
            3,
        )
    assert notifier.sent == []
