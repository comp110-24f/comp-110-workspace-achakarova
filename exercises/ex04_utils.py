"""EX04 - List Utility Functions"""

__author__: str = "730824981"


def all(list1: list[int], user_input: int) -> bool:
    """All: returns True/False if the list is equal to the input."""
    if len(list1) == 0:  # If the list is empty, return False.
        return False

    index: int = 0
    while index < len(list1):
        if list1[index] != user_input:
            return False  # If list is not the same as user_input, return False.
        index += 1  # If the current list is equal to the input, move to the next one.
    return True
    # While loop: iterates through list, if int matches user_input, return True.


def max(list2: list[int]) -> int:
    """Max: returns the largest number once found from the list."""
    index: int = 0
    largest = list2[
        0
    ]  # Sets the first number as "largest", then followed by while loop.
    if len(list2) == 0:  # If list is empty, return ValueError.
        raise ValueError("max() arg is an empty List")
    while index < len(list2):  # Iterates until the end of list2.
        if (
            list2[index] > largest
        ):  # Compares the given index of list2 to the current largest.
            largest = list2[
                index
            ]  # If the current largest is at the given index, return said int.
        index += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """is_equal: compares two lists, check if they're equal."""
    if len(list1) != len(
        list2
    ):  # Check if the lengths are different, return False if they are.
        return False

    index: int = 0
    while index < len(list1):
        while index < len(list2):
            if (
                list1[index] != list2[index]
            ):  # Check if current index of list1 is unequal to the same index of list2.
                return False  # Return False if NOT equal.
            index += 1
    return (
        True  # Return True if all indexes of list1 and equal to all indexes of list2.
    )


def extend(a: list[int], b: list[int]) -> None:
    for user_input in b:  # For loop: iterate through all values of list b.
        a.append(user_input)  # Adds each value from the list b onto list a at its end.
