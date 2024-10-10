"""Mutating functions."""

__author__ = "730824981"


def manual_append(list1: list[int], int: int) -> None:
    list1.append(int)


# manual_append is a function that has a list (list[int]) and an int as a parameter.
# mutate the list: append the int parameter to the end of the list[int] parameter.


def double(list2: list[int]) -> None:
    index: int = 0
    while index < len(list2):
        list2[index] = list2[index] * 2
        index += 1


# double is a function that has a list[int] as a parameter.
# while loop: through the list + multiply every element in the list[int] parameter by 2.

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)

# list_1 and list_2 both print [2,4,6]
