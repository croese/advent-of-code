#!/usr/bin/env python3

import itertools


def example():
    data = """1721
979
366
299
675
1456""".splitlines()

    a, b = list(
        filter(
            lambda p: p[0] + p[1] == 2020,
            itertools.combinations((int(s) for s in data), 2),
        )
    )[0]
    print(f"example: {a*b == 514579}")


def problem1(input_lines):
    a, b = list(
        filter(
            lambda p: p[0] + p[1] == 2020,
            itertools.combinations((int(s) for s in input_lines), 2),
        )
    )[0]
    print(f"problem 1: {a*b}")


def problem2(input_lines):
    a, b, c = list(
        filter(
            lambda p: p[0] + p[1] + p[2] == 2020,
            itertools.combinations((int(s) for s in input_lines), 3),
        )
    )[0]
    print(f"problem 2: {a*b*c}")


if __name__ == "__main__":
    example()

    with open("input.txt", "r") as f:
        contents = f.readlines()
        problem1(contents)
        problem2(contents)
