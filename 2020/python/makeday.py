#!/usr/bin/env python3

import sys
import os
import requests
import stat


if len(sys.argv) != 2:
    print("must provide the day number")
    exit(1)

day = sys.argv[-1]
print(f"initializing day {day}")

dir_name = f"day{day}"

try:
    os.mkdir(dir_name)
    print(f"directory {dir_name} created")
except FileExistsError:
    print(f"directory {dir_name} exists")

init_path = os.path.join(dir_name, "__init__.py")
script_path = os.path.join(dir_name, f"day{day}.py")

with open(init_path, "w") as f:
    pass

print(f"init file created")


script = f"""#!/usr/bin/env python3
 

def example():
    print("day{day}")


def problem1(input_lines):
    print("day{day}")


def problem2(input_lines):
    print("day{day}")


if __name__ == "__main__":
    example()

    with open("input.txt", "r") as f:
        contents = f.readlines()
        problem1(contents)
        problem2(contents)

"""

with open(script_path, "w") as f:
    f.write(script)

print(f"script file created")

os.chmod(script_path, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

cookie = ""
with open(".cookie", "r") as f:
    cookie = f.readline().rstrip()

headers = {
    "authority": "adventofcode.com",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    "sec-ch-ua-mobile": "?0",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": f"https://adventofcode.com/2020/day/{day}",
    "accept-language": "en-US,en;q=0.9",
    "cookie": cookie,
}

response = requests.get(
    f"https://adventofcode.com/2020/day/{day}/input", headers=headers
)

input_path = os.path.join(dir_name, "input.txt")

with open(input_path, "w") as f:
    f.write(response.text)

print(f"input file created")
