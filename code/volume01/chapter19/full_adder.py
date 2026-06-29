"""Full adder and ripple-carry binary addition."""
from code.volume01.chapter18.half_adder import half_adder
from code.volume01.chapter16.logic_gates import or_gate, validate_bit


def full_adder(a: int, b: int, carry_in: int) -> tuple[int, int]:
    validate_bit(a); validate_bit(b); validate_bit(carry_in)
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, carry_in)
    return sum2, or_gate(carry1, carry2)


def add_binary(left: str, right: str) -> str:
    if not left or not right or set(left + right) - {"0", "1"}:
        raise ValueError("inputs must be non-empty binary strings")
    max_len = max(len(left), len(right))
    left = left.zfill(max_len)
    right = right.zfill(max_len)
    carry = 0
    result: list[str] = []
    for a, b in zip(reversed(left), reversed(right)):
        bit, carry = full_adder(int(a), int(b), carry)
        result.append(str(bit))
    if carry:
        result.append("1")
    return "".join(reversed(result))
