#!/usr/bin/env python3

import re

REQUIRED_FIELDS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def example():
    data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split(
        "\n\n"
    )

    creds_batch = (
        set(dict(map(lambda s: s.split(":"), p.split())).keys()) for p in data
    )

    invalids = list(
        filter(lambda s: len(s) > 0, ((REQUIRED_FIELDS - s) for s in creds_batch))
    )

    diff = len(data) - len(invalids)

    print(f"example: {diff == 2}")


def problem1(input_lines):
    creds_batch = (
        set(dict(map(lambda s: s.split(":"), p.split())).keys()) for p in input_lines
    )

    invalids = list(
        filter(lambda s: len(s) > 0, ((REQUIRED_FIELDS - s) for s in creds_batch))
    )

    diff = len(input_lines) - len(invalids)

    print(f"problem 1: {diff}")


def valid_year(min: int, max: int, year: str) -> bool:
    return re.fullmatch(r"\d{4}", year) and (min <= int(year) <= max)


def valid_height(height: str) -> bool:
    m = re.fullmatch(r"(\d+)(in|cm)", height)
    if not m:
        return False
    elif m[2] == "in":
        return 59 <= int(m[1]) <= 76
    else:
        return 150 <= int(m[1]) <= 193


EYE_COLORS = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
VALIDATIONS = {
    "byr": lambda v: valid_year(1920, 2002, v),
    "iyr": lambda v: valid_year(2010, 2020, v),
    "eyr": lambda v: valid_year(2020, 2030, v),
    "hgt": lambda v: valid_height(v),
    "hcl": lambda v: re.fullmatch(r"#[0-9a-f]{6}", v),
    "ecl": lambda v: v in EYE_COLORS,
    "pid": lambda v: re.fullmatch(r"\d{9}", v),
    "cid": lambda v: True,
}


def validate_passport(passport) -> bool:
    return (
        all(map(lambda k: VALIDATIONS[k](passport[k]), passport))
        and len(REQUIRED_FIELDS - set(passport.keys())) == 0
    )


def problem2(input_lines):
    creds_batch = (dict(map(lambda s: s.split(":"), p.split())) for p in input_lines)

    valids = list(filter(lambda p: validate_passport(p), creds_batch))

    print(f"problem 2: {len(valids)}")


if __name__ == "__main__":
    example()

    with open("input.txt", "r") as f:
        contents = f.read().split("\n\n")
        problem1(contents)
        problem2(contents)
