from pathlib import Path

import pytest

from stocknews import constants
from stocknews.domain.errors import ConfigError
from stocknews.infrastructure.config import load_settings, parse_dotenv

STOCK = constants.ENV_STOCK_API_KEY
NEWS = constants.ENV_NEWS_API_KEY
PHONE = constants.ENV_PHONE_NUMBER


def test_parse_dotenv_reads_known_keys_quotes_and_comments() -> None:
    text = (
        "# comment\n\n"
        f"{STOCK}='abc'\n"
        f'export {NEWS}="def"\n'
        "OTHER=x\nnoequals\n"
        f"{PHONE} = +45\n"
    )
    assert parse_dotenv(text) == {STOCK: "abc", NEWS: "def", PHONE: "+45"}


def test_load_settings_reads_environment() -> None:
    env = {STOCK: "s", NEWS: "n", PHONE: "+1"}
    settings = load_settings(env, [])
    assert (settings.stock_api_key, settings.news_api_key) == ("s", "n")
    assert settings.phone_number == "+1"
    assert settings.dry_run is False


def test_load_settings_prefers_environment_over_files(tmp_path: Path) -> None:
    file = tmp_path / ".env"
    file.write_text(f"{STOCK}=file\n{NEWS}=file\n{PHONE}=file\n", encoding="utf-8")
    settings = load_settings({STOCK: "env"}, [file])
    assert settings.stock_api_key == "env"
    assert settings.news_api_key == "file"


def test_load_settings_prefers_first_file(tmp_path: Path) -> None:
    first, second = tmp_path / ".env", tmp_path / "config.env"
    first.write_text(f"{STOCK}=one\n", encoding="utf-8")
    second.write_text(f"{STOCK}=two\n{NEWS}=n\n{PHONE}=p\n", encoding="utf-8")
    settings = load_settings({}, [first, second, tmp_path / "missing.env"])
    assert settings.stock_api_key == "one"
    assert settings.news_api_key == "n"


def test_load_settings_names_missing_key() -> None:
    with pytest.raises(ConfigError, match=NEWS):
        load_settings({STOCK: "s", PHONE: "p"}, [])


def test_load_settings_requires_phone_when_sending() -> None:
    with pytest.raises(ConfigError, match=PHONE):
        load_settings({STOCK: "s", NEWS: "n"}, [])


def test_load_settings_allows_missing_phone_in_dry_run() -> None:
    settings = load_settings({STOCK: "s", NEWS: "n"}, [], dry_run=True)
    assert settings.phone_number is None
    assert settings.dry_run is True


def test_settings_repr_hides_secrets() -> None:
    settings = load_settings({STOCK: "secret", NEWS: "n", PHONE: "p"}, [])
    assert "secret" not in repr(settings)
