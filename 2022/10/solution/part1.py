from pathlib import Path

from solution.cpu import CPU


class Part1:
    def __init__(self, file: Path):
        with open(file) as f:
            self.lines = [line.strip() for line in f.readlines()]

    def solve(self) -> None:
        print("solving...")
        cpu = CPU()
        cpu.run_instructions(self.lines)
        self.signal_strength = cpu.signal_strength

    def get_result(self) -> str:
        return f"the signal strength is: {self.signal_strength}"
