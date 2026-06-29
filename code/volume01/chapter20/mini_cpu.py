"""A tiny accumulator-based CPU simulator."""
from dataclasses import dataclass


@dataclass
class MiniCPU:
    accumulator: int = 0

    def execute(self, program: list[tuple[str, int | None]]) -> list[int]:
        outputs: list[int] = []
        for instruction, value in program:
            if instruction == "LOAD":
                if value is None:
                    raise ValueError("LOAD requires a value")
                self.accumulator = value
            elif instruction == "ADD":
                if value is None:
                    raise ValueError("ADD requires a value")
                self.accumulator += value
            elif instruction == "SUB":
                if value is None:
                    raise ValueError("SUB requires a value")
                self.accumulator -= value
            elif instruction == "PRINT":
                outputs.append(self.accumulator)
            else:
                raise ValueError(f"unknown instruction: {instruction}")
        return outputs
