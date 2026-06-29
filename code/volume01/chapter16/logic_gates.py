"""Boolean logic gate functions for Volume I, Chapter 16."""

def validate_bit(value: int) -> int:
    if value not in (0, 1):
        raise ValueError("bit must be 0 or 1")
    return value


def not_gate(a: int) -> int:
    validate_bit(a)
    return 1 - a


def and_gate(a: int, b: int) -> int:
    validate_bit(a); validate_bit(b)
    return 1 if a == 1 and b == 1 else 0


def or_gate(a: int, b: int) -> int:
    validate_bit(a); validate_bit(b)
    return 1 if a == 1 or b == 1 else 0


def xor_gate(a: int, b: int) -> int:
    validate_bit(a); validate_bit(b)
    return 1 if a != b else 0
