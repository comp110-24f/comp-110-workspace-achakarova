"""Testing functions in list_fns."""

from list_fns import get_first


def test_get_first() -> None:
    assert get_first(input=["Viktorya", "Samy", "Izzi"]) == "Viktoria"
