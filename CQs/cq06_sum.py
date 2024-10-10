"""Summing the elements of a list using different loops"""

__author__ = "730824981"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    values: float = 0.0
    while index < len(vals):
        values = values + vals[index]
        index += 1
    return values


def f_sum(vals2: list[float]) -> float:
    values: float = 0.0
    for numbers in vals2:
        values = values + numbers
    return values


def f_range_sum(vals3: list[float]) -> float:
    values: float = 0.0
    for numbers in range(0, len(vals3)):
        values = values + vals3[numbers]
    return values
