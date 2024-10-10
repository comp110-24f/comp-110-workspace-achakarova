"""CQ03: While loops"""

__author__ = "730824981"


def num_instances(phrase: str, search_char: str):
    # phrase is the phrase we're searching within. It's a string.
    # search_char is the character we're searching for. It's a string.
    count: int = 0
    index: int = 0
    # Both begin at 0 and keep count of the current position.
    while index < len(phrase):
        # While loop: continues until the index is <= the length of the phrase.
        if phrase[index] == search_char:
            # Checks if the index in the phrase is equal to the search_char.
            # Index is the character at the current position.
            # Search_char is the letter (string) that we're searching for in the phrase.
            index += 1
            count += 1
            # index: increases by one, moving to the next character in phrase.
            # count: increases by one if the specified character is found.
        elif phrase[index] != search_char:
            # Elif: runs if the index in the phrase is not equal to search_char.
            index += 1
            # Increases index by one, it just keeps it moving to the next character.
    return count
