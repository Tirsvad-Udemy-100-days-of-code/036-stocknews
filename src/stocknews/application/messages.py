"""Formatting of the alert message."""

from stocknews.domain.models import Article, PriceChange

## Arrows written as escapes so the source stays ASCII.
ARROW_UP = "▲"
ARROW_DOWN = "▼"


def format_message(change: PriceChange, article: Article) -> str:
    """Build the alert message of one article.

    @param change The price change that triggered the alert.
    @param article The news article to report.
    @return Text with symbol, arrow, percentage, headline and brief.
    """
    arrow = ARROW_UP if change.percent >= 0 else ARROW_DOWN
    return (
        f"{change.symbol}: {arrow}{abs(change.percent):.1f}%\n"
        f"Headline: {article.title}\n"
        f"Brief: {article.description}"
    )
