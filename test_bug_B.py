from bug3_logic import find_max


def test_find_max_returns_largest_value():
    assert find_max([1, 3, 2]) == 3


def test_find_max_handles_negative_values():
    assert find_max([-5, -2, -9]) == -2


def test_find_max_handles_duplicate_largest_values():
    assert find_max([4, 7, 7, 1]) == 7


def test_find_max_handles_single_value():
    assert find_max([42]) == 42