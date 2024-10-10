"""EX03 - Wordle"""

__author__: str = "730824981"


def input_guess(
    secret_word_len: int,
) -> str:
    # Asks for an input until the length is correct.
    while True:
        guess = input(f"Enter a {secret_word_len}-character word: ")
        # Asks for an input with a certain length.
        if len(guess) == secret_word_len:
            return guess
        # Checks if the length of the input is correct.
        else:
            print(f"That wasn't {secret_word_len} characters! Try again.")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the character char_guess is present in the string secret_word."""

    assert len(char_guess) == 1
    return char_guess in secret_word


# Assert ensures the input is a single character.


def emojified(guess: str, secret: str) -> str:
    "Compare two strings of equal length - user guess and secret word"
    assert len(guess) == len(secret)
    # Assures that both guess and secret are equal length.

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # Green box for correct, yellow for correct character but wrong placement.
    # White for wrong character and placement.

    index: int = 0
    emojis: str = ""
    while index < len(guess):
        if guess[index] == secret[index]:
            emojis += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        index += 1
    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 0  # Counter for the number of attempts.
    won: bool = False  # Checks if player has won.
    while turns < 6 and not won:
        print("=== Turn " + str(turns + 1) + "/6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        # Gets user guess, compares length.
        print(emojified(guess, secret))
        if guess == secret:
            print("You won in " + str(turns + 1) + "/6 turns!")  # YAYY you won!
            won = True
        turns += 1
    if turns == 6:
        print("X/6 - Sorry, try again tomorrow!")  # Timeout due to exceeded attempts.


if __name__ == "__main__":
    main(secret="codes")
