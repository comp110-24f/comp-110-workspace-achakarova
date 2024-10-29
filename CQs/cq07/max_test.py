"""CQ07: Max Test"""

__author__: str = "730824981"

from find_max import find_and_remove_max


def test_find_and_remove_max_returns_value() -> None:
    list1: list[int] = [1, 5, 3, 9, 2]
    assert find_and_remove_max(list1) == 9


# Checks if the function correctly returns the largest value.


def test_find_and_remove_max_mutates_input() -> None:
    list1: list[int] = [4, 6, 6, 3, 2, 6]
    find_and_remove_max(list1)
    assert list1 == [4, 3, 2]


# Ensures the input list removes all instances of the largest number.


def test_find_and_remove_max_empty_list() -> None:
    list1: list[int] = []
    assert find_and_remove_max(list1) == -1


# Checks for empty list and covers the fact that it's equal to -1.
