"""CQ00: Functions!!"""

__author__ = "730824981"


def mimic(message: str) -> str:
    """Mimicking a message."""
    return message


def main() -> None:
    """The main function that prints the result of calling mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
