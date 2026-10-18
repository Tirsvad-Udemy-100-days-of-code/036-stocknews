import pytest

from stocknews.domain.errors import InvalidPriceError
from stocknews.domain.rules import calculate_change, is_significant


def test_calculate_change_returns_positive_percent_when_price_rises() -> None:
    assert calculate_change(100.0, 105.0) == pytest.approx(5.0)


def test_calculate_change_returns_negative_percent_when_price_falls() -> None:
    assert calculate_change(200.0, 150.0) == pytest.approx(-25.0)


@pytest.mark.parametrize("previous", [0.0, -1.0])
def test_calculate_change_raises_when_base_is_not_positive(previous: float) -> None:
    with pytest.raises(InvalidPriceError):
        calculate_change(previous, 10.0)


def test_calculate_change_raises_when_latest_is_negative() -> None:
    with pytest.raises(InvalidPriceError):
        calculate_change(10.0, -1.0)


@pytest.mark.parametrize(
    ("percent", "expected"),
    [(5.0, True), (-5.0, True), (4.99, False), (-4.99, False), (0.0, False)],
)
def test_is_significant_compares_absolute_value(percent: float, expected: bool) -> None:
    assert is_significant(percent, 5.0) is expected
