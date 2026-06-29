from code.volume01.chapter16.logic_gates import and_gate, not_gate, or_gate, xor_gate
from code.volume01.chapter18.half_adder import half_adder
from code.volume01.chapter19.full_adder import add_binary, full_adder
from code.volume01.chapter20.mini_cpu import MiniCPU


def test_logic_gates():
    assert not_gate(0) == 1
    assert not_gate(1) == 0
    assert and_gate(1, 1) == 1
    assert and_gate(1, 0) == 0
    assert or_gate(0, 1) == 1
    assert xor_gate(1, 1) == 0
    assert xor_gate(1, 0) == 1


def test_half_adder():
    assert half_adder(0, 0) == (0, 0)
    assert half_adder(1, 0) == (1, 0)
    assert half_adder(1, 1) == (0, 1)


def test_full_adder_and_binary_addition():
    assert full_adder(1, 1, 1) == (1, 1)
    assert add_binary("1010", "0011") == "1101"
    assert add_binary("1111", "1") == "10000"


def test_mini_cpu():
    cpu = MiniCPU()
    outputs = cpu.execute([("LOAD", 10), ("ADD", 5), ("SUB", 3), ("PRINT", None)])
    assert outputs == [12]
