#!/usr/bin/env python3


def binary_search(min: int, max: int, decisions: str) -> int:
    for c in decisions:
        if c == "L":
            max = min + (max - min) // 2
        else:
            min = max - (max - min) // 2

    return min


def pass_to_id(p: str) -> int:
    p = p.translate(str.maketrans({"F": "L", "B": "H", "R": "H"}))
    row_spec, col_spec = p[:7], p[7:]

    row, col = binary_search(0, 127, row_spec), binary_search(0, 7, col_spec)
    return row * 8 + col


def example():
    print(f'example 1: {pass_to_id("FBFBBFFRLR") == 357}')
    print(f'example 2: {pass_to_id("BFFFBBFRRR") == 567}')
    print(f'example 3: {pass_to_id("FFFBBBFRRR") == 119}')
    print(f'example 4: {pass_to_id("BBFFBBFRLL") == 820}')


def problem1(input_lines):
    max_id = max(map(pass_to_id, input_lines))
    print(f"problem 1: {max_id}")


def problem2(input_lines):
    ids = list(sorted(map(pass_to_id, input_lines)))
    matched_seats = list(filter(lambda p: abs(p[0] - p[1]) == 2, zip(ids, ids[1:])))[0]
    print(f"problem 2: {min(matched_seats[0], matched_seats[1]) + 1}")


if __name__ == "__main__":
    example()

    with open("input.txt", "r") as f:
        contents = list(map(lambda l: l.rstrip(), f.readlines()))
        problem1(contents)
        problem2(contents)
