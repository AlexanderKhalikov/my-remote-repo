from src.helper_functions import misha_functions
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (4, 6, 10),
    (5, 7, 12),
    (2, 2, 4),
    (3, 7, 10)
])
def test_my_sum(a, b, expected):
    assert misha_functions.my_sum(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (4, 6, 24),
    (5, 7, 35),
])
def test_my_multiply(a, b, expected):
    assert misha_functions.my_multiply(a, b) == expected

