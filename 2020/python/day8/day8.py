#!/usr/bin/env python3

from typing import Tuple


class IntcodeMachine:
    def __init__(self, instructions) -> None:
        self.ip = 0
        self.accumulator = 0
        self.ip_history = set()
        self.instructions = instructions

    def run_until_loop(self) -> int:
        while self.ip < len(self.instructions):
            if self.ip in self.ip_history:
                return self.accumulator
            else:
                self.ip_history.add(self.ip)

            opcode, operand = self._decode(self.instructions[self.ip])
            if opcode == "nop":
                # do nothing
                self.ip += 1
            elif opcode == "acc":
                self.accumulator += operand
                self.ip += 1
            elif opcode == "jmp":
                self.ip += operand
            else:
                print(f"unknown opcode: {opcode}")
                return None

    def run(self) -> int:
        while self.ip < len(self.instructions):
            if self.ip in self.ip_history:
                return None
            else:
                self.ip_history.add(self.ip)

            opcode, operand = self._decode(self.instructions[self.ip])
            if opcode == "nop":
                # do nothing
                self.ip += 1
            elif opcode == "acc":
                self.accumulator += operand
                self.ip += 1
            elif opcode == "jmp":
                self.ip += operand
            else:
                print(f"unknown opcode: {opcode}")
                return None

        return self.accumulator

    def _decode(self, instruction: str) -> Tuple[str, int]:
        opcode, operand_str = instruction.split()
        return opcode, int(operand_str)


def example():
    instructions = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()

    vm = IntcodeMachine(instructions)
    result = vm.run_until_loop()

    print(f"example: {result == 5}")


def problem1(input_lines):
    vm = IntcodeMachine(input_lines)
    result = vm.run_until_loop()

    print(f"problem 1: {result}")


def problem2(input_lines):
    find_nop_jmp = lambda p: p[1].startswith("nop") or p[1].startswith("jmp")
    transform = lambda p: (
        p[0],
        p[1].replace("nop", "jmp")
        if p[1].startswith("nop")
        else p[1].replace("jmp", "nop"),
    )
    for (index, new_op) in map(transform, filter(find_nop_jmp, enumerate(input_lines))):
        instructions_copy = input_lines[:]
        instructions_copy[index] = new_op

        vm = IntcodeMachine(instructions_copy)
        result = vm.run()
        if result:
            print(f"problem 2: {result}")
            break
    else:
        print("problem 2: none found!")


if __name__ == "__main__":
    example()

    with open("input.txt", "r") as f:
        contents = f.readlines()
        problem1(contents)
        problem2(contents)
