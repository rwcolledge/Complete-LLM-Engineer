from collections.abc import Sequence


def maximum(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values cannot be empty")
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest


def minimum(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values cannot be empty")
    smallest = values[0]
    for value in values[1:]:
        if value < smallest:
            smallest = value
    return smallest
