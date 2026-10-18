"""Command line entry point and composition root."""

import argparse
import logging
import os
import sys
from dataclasses import dataclass

from stocknews import constants
from stocknews.application.check_stock import check_stock
from stocknews.application.ports import NewsSource, Notifier, PriceSource
from stocknews.domain.errors import StockNewsError
from stocknews.infrastructure.alpha_vantage import AlphaVantagePrices
from stocknews.infrastructure.config import Settings, load_settings
from stocknews.infrastructure.console import ConsoleNotifier
from stocknews.infrastructure.news_api import NewsApiNews
from stocknews.infrastructure.whatsapp import WhatsAppNotifier

_log = logging.getLogger(__name__)

## Exit codes of the program.
EXIT_OK = 0
EXIT_ERROR = 1


@dataclass(frozen=True, slots=True)
class Services:
    """The concrete adapters handed to the use case."""

    prices: PriceSource
    news: NewsSource
    notifier: Notifier


def build_services(settings: Settings) -> Services:
    """Create the adapters: the one place that names them.

    @param settings The loaded settings.
    @return The adapters; a console notifier in dry-run mode.
    """
    notifier: Notifier
    if settings.dry_run or settings.phone_number is None:
        notifier = ConsoleNotifier()
    else:
        notifier = WhatsAppNotifier(settings.phone_number)
    return Services(
        prices=AlphaVantagePrices(settings.stock_api_key),
        news=NewsApiNews(settings.news_api_key),
        notifier=notifier,
    )


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="stocknews",
        description="Send the latest news when a stock moves by the threshold.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the messages instead of sending them",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the program.

    @param argv The arguments; None reads sys.argv.
    @return 0 when done (alert or not), 1 on a configuration or API error.
    """
    args = _parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        settings = load_settings(os.environ, dry_run=args.dry_run)
        services = build_services(settings)
        messages = check_stock(
            services.prices,
            services.news,
            services.notifier,
            constants.STOCK,
            constants.COMPANY_NAME,
            constants.THRESHOLD_PERCENT,
            constants.NEWS_COUNT,
        )
    except StockNewsError as error:
        print(f"error: {error}", file=sys.stderr)
        return EXIT_ERROR
    verb = "shown" if args.dry_run else "sent"
    _log.info("%d message(s) %s", len(messages), verb)
    return EXIT_OK
