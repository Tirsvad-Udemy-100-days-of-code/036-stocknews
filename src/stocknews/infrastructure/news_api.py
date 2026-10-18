"""NewsAPI client for the latest articles about a company."""

from stocknews import constants
from stocknews.domain.errors import ApiError
from stocknews.domain.models import Article
from stocknews.infrastructure import http


def get_news(company: str, count: int, api_key: str) -> list[Article]:
    """Fetch the latest articles about a company.

    @param company The company name to search for.
    @param count The number of articles to return.
    @param api_key The NewsAPI key.
    @return Up to count articles, newest first.
    @throws ApiError when NewsAPI does not answer with status ok.
    """
    data = http.get_json(
        constants.NEWS_ENDPOINT,
        {
            "q": company,
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": count,
            "apiKey": api_key,
        },
        constants.HTTP_TIMEOUT_SECONDS,
    )
    if data.get("status") != "ok":
        raise ApiError(f"NewsAPI: {data.get('message', 'unknown error')}")
    raw_articles = data.get("articles", [])
    return [
        Article(
            title=str(raw.get("title") or ""),
            description=str(raw.get("description") or ""),
        )
        for raw in raw_articles[:count]
    ]


class NewsApiNews:
    """NewsSource backed by NewsAPI."""

    def __init__(self, api_key: str) -> None:
        """Keep the API key.

        @param api_key The NewsAPI key.
        """
        self._api_key = api_key

    def get_news(self, company: str, count: int) -> list[Article]:
        """Return at most count articles about the company, newest first."""
        return get_news(company, count, self._api_key)
