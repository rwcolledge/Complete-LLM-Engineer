"""Half adder implementation."""
from code.volume01.chapter16.logic_gates import and_gate, xor_gate, validate_bit


def half_adder(a: int, b: int) -> tuple[int, int]:
    validate_bit(a); validate_bit(b)
    return xor_gate(a, b), and_gate(a, b)
