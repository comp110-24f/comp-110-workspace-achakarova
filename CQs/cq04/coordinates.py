"""CQ04: Coordinates"""

__author__: str = "730824981"


def get_coords(xs: str, ys: str) -> None:
    index1 = 0
    index2 = 0
    while index1 < len(xs):
        while index2 < len(ys):
            # Print the formatted pair
            print(f"({xs[index1]},{ys[index2]})")
            index2 += 1
        index1 += 1
