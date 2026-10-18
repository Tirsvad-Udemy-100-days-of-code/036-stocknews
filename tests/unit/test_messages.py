from stocknews.application.messages import ARROW_DOWN, ARROW_UP, format_message
from stocknews.domain.models import Article, PriceChange

ARTICLE = Article("Big news", "Short brief")


def test_format_message_uses_up_arrow_when_price_rises() -> None:
    change = PriceChange("TSLA", 100.0, 105.0, 5.0)
    assert format_message(change, ARTICLE) == (
        f"TSLA: {ARROW_UP}5.0%\nHeadline: Big news\nBrief: Short brief"
    )


def test_format_message_uses_down_arrow_when_price_falls() -> None:
    change = PriceChange("TSLA", 100.0, 94.0, -6.0)
    assert format_message(change, ARTICLE).startswith(f"TSLA: {ARROW_DOWN}6.0%")
