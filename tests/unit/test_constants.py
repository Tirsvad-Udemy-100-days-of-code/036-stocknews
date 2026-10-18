from stocknews import constants


def test_threshold_is_positive_percent() -> None:
    assert 0 < constants.THRESHOLD_PERCENT < 100


def test_news_count_is_three() -> None:
    assert constants.NEWS_COUNT == 3


def test_stock_and_company_are_set() -> None:
    assert constants.STOCK
    assert constants.COMPANY_NAME
