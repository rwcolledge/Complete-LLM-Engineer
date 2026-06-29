from code.volume01.chapter14.algorithms import maximum, minimum


def test_maximum() -> None:
    assert maximum([3, 1, 9, 2]) == 9


def test_minimum() -> None:
    assert minimum([3, 1, 9, 2]) == 1
