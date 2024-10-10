"""CQ02: Conditionals"""

__author__ = "730824981"


def guess_a_number() -> None:
    user_input = input("Guess a number:")
    print("Your guess was " + user_input)
    if int(user_input) == 7:
        print("You got it!")
    elif int(user_input) < 7:
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was too high! The secret number is 7")
    return None


if __name__ == "__main__":
    guess_a_number()
