"""CQ04: Concatenation"""

__author__: str = "730824981"


def concat(a: str, b: str) -> str:
    """Concat: Combine two strings and return them together."""
    return a + b


word1 = "happy"  # Word1, word2 are global variables
word2 = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
