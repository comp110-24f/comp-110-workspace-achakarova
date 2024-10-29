"""EX05: Utilities"""

__author__: str = "730824981"


def only_evens(nums: list[int]) -> list[int]:
    """Return a list containing only the even integers from the input list."""
    result = []
    index = 0
    while index < len(nums):  # while loop: check each number in nums.
        if nums[index] % 2 == 0:  # Check if the number is even (divisible by 2).
            result.append(nums[index])  # Even numbers get added to result.
        index += 1
    return result


def sub(list1: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start = 0
    if end > len(list1):
        end = len(list1)  # Start and end are within bounds of list1.
    if len(list1) == 0 or start >= len(list1) or end <= 0:
        return []  # Empty if not within bounds.
    new_list: list[int] = []
    for ints in range(start, end):  # Iterates through range, selects ints in list1.
        new_list.append(list1[ints])  # Adds list1 ints to new_list.
    return new_list


def add_at_index(list1: list[int], element: int, index: int) -> None:
    if index < 0 or index > len(list1):
        raise IndexError("Index is out of bounds for the input list.")
    list1.append(0)  # Extend list with a temporary number.
    for num in range(len(list1) - 1, index, -1):
        list1[num] = list1[num - 1]  # Uses a loop to shift elements back one (-1).
    list1[index] = element  # Adds element at specified index.
    return
