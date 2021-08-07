#!/usr/bin/env python3


class PasswordChecker:
    def __init__(self, rule: str) -> None:
        range, self.char = rule.split(" ")
        self.pos1, self.pos2 = map(lambda c: int(c), range.split("-"))

    def check(self, password: str) -> bool:
        return self.pos1 <= password.count(self.char) <= self.pos2


class CorporatePasswordChecker(PasswordChecker):
    def check(self, password: str) -> bool:
        at_pos1 = password[self.pos1 - 1] == self.char
        at_pos2 = password[self.pos2 - 1] == self.char
        return at_pos1 != at_pos2


def example():
    lines = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()

    count = len(
        list(
            filter(
                lambda p: PasswordChecker(p[0]).check(p[1]),
                (tuple(l.split(": ")) for l in lines),
            )
        )
    )
    print(f"example: {count == 2}")


def problem1(input_lines):
    count = len(
        list(
            filter(
                lambda p: PasswordChecker(p[0]).check(p[1]),
                (tuple(l.split(": ")) for l in input_lines),
            )
        )
    )
    print(f"day1: {count}")


def problem2(input_lines):
    count = len(
        list(
            filter(
                lambda p: CorporatePasswordChecker(p[0]).check(p[1]),
                (tuple(l.split(": ")) for l in input_lines),
            )
        )
    )
    print(f"day2: {count}")


if __name__ == "__main__":
    example()

    with open("input.txt", "r") as f:
        contents = f.readlines()
        problem1(contents)
        problem2(contents)
