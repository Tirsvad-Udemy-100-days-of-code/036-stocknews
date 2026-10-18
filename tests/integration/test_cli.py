from pathlib import Path

import pytest

from stocknews import constants
from stocknews.domain.errors import ApiError
from stocknews.domain.models import Article
from stocknews.infrastructure.alpha_vantage import AlphaVantagePrices
from stocknews.infrastructure.config import Settings
from stocknews.infrastructure.console import ConsoleNotifier
from stocknews.infrastructure.whatsapp import WhatsAppNotifier
from stocknews.presentation import cli


class FakePrices:
    def __init__(self, closes: tuple[float, float] | None) -> None:
        self.closes = closes

    def get_stock_prices(self, symbol: str) -> tuple[float, float]:
        if self.closes is None:
            raise ApiError("quota reached")
        return self.closes


class FakeNews:
    def get_news(self, company: str, count: int) -> list[Article]:
        return [Article("Headline", "Brief")]


class FakeNotifier:
    def __init__(self) -> None:
        self.sent: list[str] = []

    def send_message(self, text: str) -> None:
        self.sent.append(text)


@pytest.fixture(autouse=True)
def isolated_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv(constants.ENV_STOCK_API_KEY, "s")
    monkeypatch.setenv(constants.ENV_NEWS_API_KEY, "n")
    monkeypatch.delenv(constants.ENV_PHONE_NUMBER, raising=False)


def install(
    monkeypatch: pytest.MonkeyPatch, closes: tuple[float, float] | None
) -> FakeNotifier:
    notifier = FakeNotifier()
    services = cli.Services(FakePrices(closes), FakeNews(), notifier)
    monkeypatch.setattr(cli, "build_services", lambda settings: services)
    return notifier


def test_main_returns_zero_and_sends_when_change_is_large(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(constants.ENV_PHONE_NUMBER, "+45")
    notifier = install(monkeypatch, (100.0, 110.0))
    assert cli.main([]) == 0
    assert len(notifier.sent) == 1


def test_main_returns_zero_and_sends_nothing_when_change_is_small(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    notifier = install(monkeypatch, (100.0, 100.5))
    assert cli.main(["--dry-run"]) == 0
    assert notifier.sent == []


def test_main_returns_one_and_reports_on_stderr_when_api_fails(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    install(monkeypatch, None)
    assert cli.main(["--dry-run"]) == 1
    assert "quota reached" in capsys.readouterr().err


def test_main_returns_one_when_setting_is_missing(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.delenv(constants.ENV_NEWS_API_KEY)
    install(monkeypatch, (100.0, 110.0))
    assert cli.main(["--dry-run"]) == 1
    assert constants.ENV_NEWS_API_KEY in capsys.readouterr().err


def test_build_services_uses_console_notifier_in_dry_run() -> None:
    services = cli.build_services(Settings("s", "n", None, True))
    assert isinstance(services.notifier, ConsoleNotifier)
    assert isinstance(services.prices, AlphaVantagePrices)


def test_build_services_uses_whatsapp_notifier_when_sending() -> None:
    services = cli.build_services(Settings("s", "n", "+45", False))
    assert isinstance(services.notifier, WhatsAppNotifier)
