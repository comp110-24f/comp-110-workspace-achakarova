"""EX06: Dictionary Utilities"""

__author__: str = "730824981"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values of the dictionary."""
    dict2: dict[str, str] = {}
    for key in dict1:  # Loop through each key in the dictionary1.
        value: str = dict1[key]
        if (
            value in dict2
        ):  # Check if this is already a key in dict2 to not have duplication.
            raise KeyError("Two keys are not the same.")
        else:
            dict2[value] = key  # Set the value as a key in dict2.
    return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns most popular color from the dictionary."""
    count: dict[str, int] = {}  # Emptry dictionary.
    favorite: str = ""  # Most popular color.
    counting: int = 0  # Index, stores most popular color.
    for name in dict1:
        color: str = dict1[name]  # Get the color for the current name.
        if color in count:
            count[color] += 1  # Increase increment if color is already a key in count.
        else:
            count[color] = 1
    for color in count:  # Loop through count to find the most popular color.
        if count[color] > counting:
            favorite = color
            counting = count[color]
            # If the current color's count is greater than the highest found count,
            # update favorite and counting to said color's instances found.
    return favorite


def count(list1: list[str]) -> dict[str, int]:
    store: dict[str, int] = {}
    for item in list1:
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    return store


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Puts the words in dictionary sorted by alphabetical order."""
    dict2: dict[str, list[str]] = {}
    for word in list1:  # Check if the first letter is already a key,
        if word:
            letter = word[0].lower()
            if letter in dict2:
                dict2[letter].append(word)
            # Append the word to the existing list for that letter.
            else:
                dict2[letter] = [word]
    return dict2


def update_attendance(dict: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance by using days of the week as dictionary keys."""
    if day in dict and student not in dict[day]:
        dict[day].append(student)
    elif day not in dict:
        dict[day] = [student]
    return None
