import urllib.error

import pytest

from stocknews.domain.errors import ApiError
from stocknews.infrastructure import http


def test_get_json_returns_object_and_encodes_params(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    urls: list[str] = []

    def fake_open(url: str, timeout: float) -> bytes:
        urls.append(url)
        return b'{"a": 1}'

    monkeypatch.setattr(http, "open_url", fake_open)
    assert http.get_json("https://x.test/q", {"k": "a b", "n": 3}, 5) == {"a": 1}
    assert urls == ["https://x.test/q?k=a+b&n=3"]


@pytest.mark.parametrize("body", [b"not json", b"[1, 2]"])
def test_get_json_raises_api_error_when_body_is_not_an_object(
    monkeypatch: pytest.MonkeyPatch, body: bytes
) -> None:
    monkeypatch.setattr(http, "open_url", lambda url, timeout: body)
    with pytest.raises(ApiError):
        http.get_json("https://x.test", {}, 5)


def test_get_json_raises_api_error_without_leaking_url_on_network_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail(url: str, timeout: float) -> bytes:
        raise urllib.error.URLError("offline")

    monkeypatch.setattr(http, "open_url", fail)
    with pytest.raises(ApiError, match="offline") as info:
        http.get_json("https://x.test", {"apikey": "SECRET"}, 5)
    assert "SECRET" not in str(info.value)


def test_open_url_returns_body(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeResponse:
        def __enter__(self) -> "FakeResponse":
            return self

        def __exit__(self, *args: object) -> None:
            return None

        def read(self) -> bytes:
            return b"body"

    seen: list[float] = []

    def fake_urlopen(url: str, timeout: float) -> FakeResponse:
        seen.append(timeout)
        return FakeResponse()

    monkeypatch.setattr(http.urllib.request, "urlopen", fake_urlopen)
    assert http.open_url("https://x.test", 7) == b"body"
    assert seen == [7]
