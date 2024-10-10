"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730824981"


def input_word() -> str:
    user_input = input("Enter a 5-character word: ")  # Asks for a 5-letter word
    if len(user_input) == 5:  # If input length is exactly 5, it will print result.
        print(user_input)
    elif (
        len(user_input) != 5
    ):  # If input length isn't 5, give error message but still print.
        print("Error: Word must contain 5 characters.")
        print(user_input)
    return user_input


def input_letter() -> str:
    user_input = input("Enter a single character: ")  # Asks for a single character.
    if len(user_input) == 1:  # If the length of the input is exactly 1, print input.
        print(user_input)
    elif (
        len(user_input) != 1
    ):  # If length of input isn't 1, print error message, then print input.
        print("Error: Character must be a single character.")
        print(user_input)
    return user_input


def contains_char(word: str, letter: str) -> None:
    index: int = 0  # Index for iterating through word
    count: int = 0  # Count for occurrences of the letter
    print("Searching for " + str(letter) + " in " + str(word))
    while index < len(word):  # Loop through each character in the word
        if word[index] == letter:  # Check if current character matches the letter
            print(
                letter + " found at index " + str(index)
            )  # Print the index where it's found
            count += 1
        index += 1  # Move to next index
    if count == 0:  # If no instances were found
        print(
            "No instances of " + str(letter) + " found in " + str(word)
        )  # Indicate no matches
    elif count > 0:  # If at least one instance was found
        print(
            str(count) + " instances of " + str(letter) + " found in " + str(word)
        )  # Print count of occurrences


contains_char(word=input_word(), letter=input_letter())
