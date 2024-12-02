"""File to define Bear class."""

__author__: str = "730824981"


class Bear:
    """Represent the bear's age and hunger."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a Bear with age set to 0 and hunger score set to 0."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """One day passing, increase bear age by one, decrease hunger by one."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase the bear's hunger score by the number of fish eaten."""
        self.hunger_score += num_fish
