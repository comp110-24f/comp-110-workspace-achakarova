"""Welcome to Dog110!"""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """Determine if all dogs were good at daycare."""
    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = len(scores) == idx + 1

    # Add the following functionality:
    # If the dog is good...
    if is_good:
        print(f"Good dog, {scores[idx]["name"]}!")
        # Is it the last dog?
        if is_last:
            return True
        else:
            return all_good(scores, thresh, idx + 1)
    # Otherwise... 2nd base case
    else:
        return False


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]
