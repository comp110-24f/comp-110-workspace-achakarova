"""A tea party planner."""

__author__: str = "730824981"


def main_planner(guests: int) -> None:
    """Lists everything: the number of items and their cost for x amount of guests."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return None


# It takes all the functions below and puts guests in them as an input.
# It prints the result for each.
# I thought we had to define guests=people.
# But we don't because people and guests are both an int.
# main_planner function is #1 and puts guests directly into tea_bags and treats.
# These functions use people to calculate their values.
# Guests are input and serve the same role as people.
# I also had issues with the quotes, but was able to figure it out.


def tea_bags(people: int) -> int:
    """Finds the number of tea needed for x amount of guests."""
    return people * 2


# It returns the amount of people multiplied by two.
# People is the parameter, which is an integer number.


def treats(people: int) -> int:
    """Finds the number of treats per guest, based on drinks."""
    return int(tea_bags(people) * 1.5)


# Calls tea_bags(people), which is already multiplied by two.
# It then multiplies it by 1.5 and returns the value for treats.
# I had to think about where to put the int part for the return statement.


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of tea bags + treats."""
    return (tea_count * 0.5) + (treat_count * 0.75)


# Multiplies tea_count by 0.5 and treat_count by 0.75.
# Returns the total cost.
# Why do we use tea_count instead of tea_bags (for example)?
# Count is after tea_bags are called. tea_bags calculates count.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
