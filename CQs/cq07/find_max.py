"""CQ07: Find Max"""

__author__: str = "730824981"


def find_and_remove_max(list1: list[int]) -> int:
    """Find, return, and remove all instances of the largest number in the list."""
    if len(list1) == 0:  # If the list is empty, return -1.
        return -1

    index: int = 0
    largest = list1[0]
    while index < len(
        list1
    ):  # While loop iterates through the list to find the largest number.
        if list1[index] > largest:
            largest = list1[
                index
            ]  # Largest variable is updated whenever a larger value is found.
        index += 1

    index = 0
    while index < len(list1):  # Checks each element in the list.
        if list1[index] == largest:
            list1.pop(index)  # Removes all instances of the largest number.
        else:
            index += 1
    return largest
