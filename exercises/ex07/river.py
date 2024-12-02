"""File to define River class."""

__author__: str = "730824981"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Represents the fish and bears on a river during a given day."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes Fish older than 3 years and Bears older than 5 years."""
        new_fish: list[Fish] = []  # Empty list to hold younger fish.
        new_bears: list[Bear] = []  # Empty list to hold younger bears.

        for fish in self.fish:  # Loop through each fish in the river and check its age.
            if fish.age <= 3:  # Keep fish if age is 3 or less.
                new_fish.append(
                    fish
                )  # Add fish to the list if it meets the age requirement.

        for (
            bear
        ) in self.bears:  # Loop through each bear in the river and check its age.
            if bear.age <= 5:  # Keep bear if age is 5 or less.
                new_bears.append(
                    bear
                )  # Add bear to the list if it meets the age requirement.

        self.fish = new_fish  # Update the fish list with only the younger fish.
        self.bears = new_bears  # Update the bears list with only the younger bears.

    def remove_fish(self, amount: int):
        """Remove a specified amount of Fish from the River."""
        fish: int = 0
        while fish < amount:
            self.fish.pop(0)  # Remove the first fish from the list.
            fish += 1
        return None

    def bears_eating(self):
        """Allow each bear to eat 3 fish if there are enough fish in the river."""
        if len(self.fish) >= 3:  # Ensure there are enough fish for at least one bear
            for bear in self.bears:
                # Only allow the bear to eat if there are at least 3 fish available
                if len(self.fish) >= 3:
                    self.remove_fish(3)
                    bear.eat(3)

    def check_hunger(self):
        """Remove bears with a hunger score below zero from the river."""
        new_bear: list[Bear] = []  # Empty list to store bears with zero hunger.
        for bears in self.bears:
            if bears.hunger_score >= 0:  # Keep bear if hunger score is 0 or above
                self.bears.append(
                    bears
                )  # Add bear to new list if it meets the hunger requirement
        self.bear = (
            new_bear  # Bear population only remains with hunger score of 0 or more.
        )
        return None

    def repopulate_fish(self):
        """Repopulate the river with new fish based on the current fish population."""
        n = (len(self.fish) // 2) * 4
        count = 0
        while count < n:
            self.fish.append(Fish())
            count += 1
        return None

    def repopulate_bears(self):
        """Repopulate the river with new bears based on the current bear population."""
        n = len(self.bears) // 2
        count = 0
        while count < n:
            self.bears.append(Bear())
            count += 1
        return None

    def view_river(self):
        """Display the current day and the population of fish and bears in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Creates a week by calling one_river_day 7 times."""
        idx: int = 0
        while idx < 7:  # Repeat for 7 days.
            self.one_river_day()
            idx += 1
        return None
