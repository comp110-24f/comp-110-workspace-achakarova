"""File to define Fish class."""

__author__: str = "730824981"


class Fish:
    """Represents the fish's age."""

    age: int

    def __init__(self):
        """Initialize a fish with age 0."""
        self.age: int = 0
        return None

    def one_day(self):
        """One day passing, increase fish age by one."""
        self.age += 1
        return None
