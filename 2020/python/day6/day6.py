#!/usr/bin/env python3

import functools


def example():
    data = """abc

a
b
c

ab
ac

a
a
a
a

b""".split(
        "\n\n"
    )

    counts = map(
        lambda g: len(
            functools.reduce(
                lambda accum, curr: accum | curr, (set(s) for s in g.split())
            )
        ),
        data,
    )

    print(f"example: {sum(counts) == 11}")


def problem1(input_lines):
    counts = map(
        lambda g: len(
            functools.reduce(
                lambda accum, curr: accum | curr, (set(s) for s in g.split())
            )
        ),
        input_lines,
    )

    print(f"problem 1: {sum(counts)}")


def problem2(input_lines):
    counts = map(
        lambda g: len(
            functools.reduce(
                lambda accum, curr: accum & curr, (set(s) for s in g.split())
            )
        ),
        input_lines,
    )

    print(f"problem 2: {sum(counts)}")


if __name__ == "__main__":
    example()

    with open("input.txt", "r") as f:
        contents = f.read().split("\n\n")
        problem1(contents)
        problem2(contents)
