"""Generate truth tables for common logic gates."""
from code.volume01.chapter16.logic_gates import and_gate, or_gate, xor_gate


def rows():
    for a in (0, 1):
        for b in (0, 1):
            yield a, b


def print_truth_tables() -> None:
    print("A B AND OR XOR")
    for a, b in rows():
        print(a, b, and_gate(a, b), or_gate(a, b), xor_gate(a, b))


if __name__ == "__main__":
    print_truth_tables()
