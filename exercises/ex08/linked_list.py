"""Exploring linked list utils in class."""

from __future__ import annotations

__author__: str = "730824981"


class Node:
    """Represents a node in a linked list."""

    value: int  # The value stored in the node.
    next: (
        Node | None
    )  # The next node in the linked list, or None if this is the last node.

    def __init__(self, val: int, next: Node | None):
        """Initialize a Node with a value and a reference to the next node."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = ""
        if (
            self.next is None
        ):  # Base case: If the current node's next is None, return "None".
            rest = "None"
        else:
            rest = str(self.next)  # Recursive case: Call __str__ on the next node.
        return f"{self.value} -> {rest}"


def recursive_range(start: int, end: int) -> Node | None:
    """Creates linked list with values from start to end."""
    # Edge case: If start > end, raise a ValueError.
    if start > end:
        raise ValueError("Start cannot be greater than end.")
    # Base case: If start == end, return None (empty list).
    if start == end:
        return None
    # Recursive case -- call function again!
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    if head.next is None:  # Base case: when "head" is the last node
        return head.value
    else:  # Recursive case
        return last(head.next)


two: Node = Node(2, None)
one: Node = Node(1, two)


def value_at(head: Node | None, index: int) -> int:
    """Retrieve the value at a specific index in a linked list."""
    if (
        head is None
    ):  # Edge Case: If head is None, raise IndexError for the too short list.
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # Base Case: If index == 0, return the current node's value.
        return head.value
    else:  # Recursive Case
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Find the maximum value in a linked list."""
    if head is None:  # Edge Case: Raise ValueError if the list is empty.
        raise ValueError("Cannot call max with None.")
    if head.next is None:  # Base Case: If next Node is None, return current Node value.
        return head.value
    highest: int = max(head.next)
    if head.value > highest:  # Recursive Case:
        # Compare the current node's value with the max of the list.
        highest = head.value
    return highest


def linkify(items: list[int]) -> Node | None:
    """Convert a list of integers into a linked list."""
    if len(items) == 0:  # Base Case: If the list is empty, return None.
        return None
    else:  # Recursive Case: Create a node with the first item and recurse.
        first: int = items[0]
        rest: Node | None = linkify(items[1:])
        return Node(first, rest)


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale all values in a linked list by a given factor."""
    if head is None:  # Base Case: If head is None, return None.
        return None
    else:  # Recursive Case: Scale the current node's value and recurse.
        first: int = head.value * factor
        rest: Node | None = scale(head.next, factor)
        return Node(first, rest)
