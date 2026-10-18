from typing import Any

import pytest

from stocknews import constants
from stocknews.domain.errors import ApiError
from stocknews.domain.models import Article
from stocknews.infrastructure import http, news_api


def serve(monkeypatch: pytest.MonkeyPatch, payload: dict[str, Any]) -> list[Any]:
    calls: list[Any] = []

    def fake(url: str, params: dict[str, Any], timeout: float) -> dict[str, Any]:
        calls.append((url, params))
        return payload

    monkeypatch.setattr(http, "get_json", fake)
    return calls


def test_get_news_returns_articles_and_sends_query(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    payload = {
        "status": "ok",
        "articles": [
            {"title": "A", "description": "a"},
            {"title": "B", "description": None},
            {"title": "C", "description": "c"},
            {"title": "D", "description": "d"},
        ],
    }
    calls = serve(monkeypatch, payload)
    articles = news_api.NewsApiNews("KEY").get_news("Tesla Inc", 3)
    assert articles == [Article("A", "a"), Article("B", ""), Article("C", "c")]
    url, params = calls[0]
    assert url == constants.NEWS_ENDPOINT
    assert params["sortBy"] == "publishedAt"
    assert params["language"] == "en"
    assert params["pageSize"] == 3
    assert params["q"] == "Tesla Inc"


def test_get_news_returns_empty_list_when_no_articles_key(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    serve(monkeypatch, {"status": "ok"})
    assert news_api.get_news("Tesla Inc", 3, "KEY") == []


def test_get_news_raises_when_status_is_not_ok(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    serve(monkeypatch, {"status": "error", "message": "bad key"})
    with pytest.raises(ApiError, match="bad key"):
        news_api.get_news("Tesla Inc", 3, "KEY")


def test_get_news_raises_with_default_message_when_none_given(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    serve(monkeypatch, {"status": "error"})
    with pytest.raises(ApiError, match="unknown error"):
        news_api.get_news("Tesla Inc", 3, "KEY")
