"""EX05: Utils Test"""

__author__: str = "730824981"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# Tests for only_evens
def test_only_evens_empty():
    """Edge case: Test with an empty list."""
    assert only_evens([]) == []


def test_only_evens_odd():
    """Use case: Test with a list of odd numbers."""
    assert only_evens([1, 3, 5, 7]) == []


def test_only_evens_mixed():
    """Use case: Test with a list with mixed odd and even numbers."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


# Tests for sub
def test_sub_indices():
    """Edge case: Test what happens if start and end indices are out of list bounds."""
    assert sub([10, 20, 30, 40], -5, 10) == [10, 20, 30, 40]


def test_sub_part():
    """Use case: Test with a part of the values from the list."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_no_mutation():
    """No mutation test: No modifications to the original list."""
    lst = [5, 10, 15]
    sub(lst, 0, 2)
    assert lst == [5, 10, 15]


# Tests for add_at_index
def test_add_at_index_invalid():
    """Edge case: Test if it raises IndexError for an invalid index."""
    lst = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(lst, 99, 10)


def test_add_at_index_insert():
    """Use case: Test what occurs when inserting an element in the middle."""
    lst = [1, 2, 3]
    add_at_index(lst, 99, 1)
    assert lst == [1, 99, 2, 3]


def test_add_at_index_no_mutation_for_incorrect_index():
    """Mutation test: Ensure add_at_index does not modify list if index is invalid."""
    lst = [1, 2, 3]
    try:
        add_at_index(lst, 99, -1)
    except IndexError:
        pass
    assert lst == [1, 2, 3]
