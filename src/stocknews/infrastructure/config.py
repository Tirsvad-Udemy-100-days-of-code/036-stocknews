"""Settings from environment variables and local .env files."""

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path

from stocknews import constants
from stocknews.domain.errors import ConfigError

## The only keys read from a .env file.
_KNOWN_KEYS = (
    constants.ENV_STOCK_API_KEY,
    constants.ENV_NEWS_API_KEY,
    constants.ENV_PHONE_NUMBER,
)

## Files read from the working directory, the first one wins.
DEFAULT_DOTENV_PATHS = (Path(".env"), Path("config.env"))

_QUOTES = ("'", '"')


@dataclass(frozen=True, slots=True)
class Settings:
    """The settings of one run. Holds secrets: never log it.

    @param stock_api_key The Alpha Vantage key.
    @param news_api_key The NewsAPI key.
    @param phone_number The recipient, or None in dry-run mode.
    @param dry_run Print the messages instead of sending them.
    """

    stock_api_key: str
    news_api_key: str
    phone_number: str | None
    dry_run: bool

    def __repr__(self) -> str:
        """Hide the secrets."""
        return f"Settings(dry_run={self.dry_run})"


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in _QUOTES:
        return value[1:-1]
    return value


def parse_dotenv(text: str) -> dict[str, str]:
    """Parse KEY=VALUE lines, keeping only the known keys.

    @param text The content of a .env file.
    @return The known keys that the text sets.
    """
    values: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip().removeprefix("export ")
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        if key in _KNOWN_KEYS:
            values[key] = _unquote(value.strip())
    return values


def _read_dotenv(path: Path) -> dict[str, str]:
    try:
        return parse_dotenv(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


def _require(values: Mapping[str, str], name: str) -> str:
    value = values.get(name, "")
    if not value:
        raise ConfigError(f"missing setting {name}")
    return value


def load_settings(
    environ: Mapping[str, str],
    dotenv_paths: Iterable[Path] = DEFAULT_DOTENV_PATHS,
    dry_run: bool = False,
) -> Settings:
    """Load the settings; environment variables beat the files.

    @param environ The environment variables.
    @param dotenv_paths Files to read, the earlier file wins.
    @param dry_run Whether the run only prints the messages.
    @return The settings.
    @throws ConfigError naming a missing setting.
    """
    values: dict[str, str] = {}
    for path in reversed(list(dotenv_paths)):
        values.update(_read_dotenv(path))
    values.update({k: environ[k] for k in _KNOWN_KEYS if environ.get(k)})
    phone = values.get(constants.ENV_PHONE_NUMBER) or None
    if phone is None and not dry_run:
        raise ConfigError(f"missing setting {constants.ENV_PHONE_NUMBER}")
    return Settings(
        stock_api_key=_require(values, constants.ENV_STOCK_API_KEY),
        news_api_key=_require(values, constants.ENV_NEWS_API_KEY),
        phone_number=phone,
        dry_run=dry_run,
    )
