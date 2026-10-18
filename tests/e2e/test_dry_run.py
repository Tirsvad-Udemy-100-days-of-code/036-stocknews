import json
import runpy
import sys
from pathlib import Path

import pytest

from stocknews import constants
from stocknews.__main__ import main as entry_main
from stocknews.infrastructure import http
from stocknews.presentation import cli


def fake_open(url: str, timeout: float) -> bytes:
    if url.startswith(constants.STOCK_ENDPOINT):
        series = {
            "2026-10-15": {constants.CLOSE_KEY: "100.0"},
            "2026-10-16": {constants.CLOSE_KEY: "94.0"},
        }
        return json.dumps({constants.SERIES_KEY: series}).encode()
    articles = [{"title": f"Title {i}", "description": f"Brief {i}"} for i in range(5)]
    return json.dumps({"status": "ok", "articles": articles}).encode()


def test_dry_run_prints_messages_without_phone_or_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv(constants.ENV_STOCK_API_KEY, "s")
    monkeypatch.setenv(constants.ENV_NEWS_API_KEY, "n")
    monkeypatch.delenv(constants.ENV_PHONE_NUMBER, raising=False)
    monkeypatch.setattr(http, "open_url", fake_open)
    assert cli.main(["--dry-run"]) == 0
    out = capsys.readouterr().out
    assert out.count("TSLA: ") == constants.NEWS_COUNT
    assert "6.0%" in out
    assert "Headline: Title 0" in out
    assert "Brief: Brief 2" in out


def test_entry_point_is_the_cli_main() -> None:
    assert entry_main is cli.main


def test_module_run_exits_with_main_code(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv(constants.ENV_STOCK_API_KEY, raising=False)
    monkeypatch.setattr(sys, "argv", ["stocknews", "--dry-run"])
    with pytest.raises(SystemExit) as info:
        runpy.run_module("stocknews", run_name="__main__")
    assert info.value.code == 1
