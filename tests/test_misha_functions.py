from src.helper_functions import misha_functions


def test_my_sum():
    assert misha_functions.my_sum(4, 6) == 10
    assert misha_functions.my_sum(5, 7) == 12
    assert misha_functions.my_sum(2, 2) == 4


def test_my_multiply():
    assert misha_functions.my_multiply(3, 4) == 12
    assert misha_functions.my_multiply(4, 6) == 24

