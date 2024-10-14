"""Summing the elements of a list using different loops"""

__author__ = "730824981"


def w_sum(vals: list[float]) -> float:
    # Returns the sum of all elements in the list named vals.
    index: int = 0
    values: float = 0.0
    while index < len(vals):
        # Loops until the index reaches the length of the list.
        values = values + vals[index]
        # Adds the value at the current index to the values sum.
        index += 1
    return values


def f_sum(vals2: list[float]) -> float:
    # Calculates the sum of all the elements in the list vals2.
    values: float = 0.0
    for numbers in vals2:
        # For loop
        values = values + numbers
        #  Adds the current numbers to values.
    return values


def f_range_sum(vals3: list[float]) -> float:
    # Calculates the sum of all elements in vals.
    values: float = 0.0
    for numbers in range(0, len(vals3)):
        # For.. in range(...) loop.
        values = values + vals3[numbers]
    return values
