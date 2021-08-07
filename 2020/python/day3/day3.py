#!/usr/bin/env python3

from functools import reduce
import functools


OPEN_SPACE = "."
TREE_SPACE = "#"


def count_trees(map_rows, right_delta: int, down_delta: int) -> int:
    positions = (
        (d * down_delta, (d * right_delta) % len(map_rows[0]))
        for d in range(0, len(map_rows) // down_delta)
    )

    tree_positions = filter(lambda p: map_rows[p[0]][p[1]] == TREE_SPACE, positions)
    count = len(list(tree_positions))

    return count


def example():
    rows = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()

    count = count_trees(rows, 3, 1)

    print(f"example: {count == 7}")


def problem1(input_lines):
    print(f"problem 1: {count_trees(input_lines, 3, 1)}")


def problem2(input_lines):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = functools.reduce(
        lambda x, y: x * y, (count_trees(input_lines, r, d) for (r, d) in slopes)
    )
    print(f"problem 2: {product}")


if __name__ == "__main__":
    example()

    with open("input.txt", "r") as f:
        contents = list(map(lambda l: l.rstrip(), f.readlines()))
        problem1(contents)
        problem2(contents)
