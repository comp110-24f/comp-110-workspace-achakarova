"""EX04 - List Utility Functions"""

__author__: str = "730824981"


def all(list1: list[int], given: int) -> bool:
    """aaaaa"""
    if len(list1) == 0:
        return False
    for num in list1:
        if num != given:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
