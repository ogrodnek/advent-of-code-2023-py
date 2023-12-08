import itertools
from typing import Iterator
import re


def parse_directions(line: str) -> Iterator[int]:
    directions = [0 if c == "L" else 1 for c in list(line.strip())]
    return itertools.cycle(directions)

def parse_map(lines: list[str]) -> dict[str, tuple[str, str]]:
    map = {}
    pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    
    for line in lines:
        match = pattern.match(line)
        if match:
            map[match.group(1)] = (match.group(2), match.group(3))
        
    return map

with open("input.txt") as f:
    directions = parse_directions(f.readline())
    f.readline()
    map = parse_map(f.readlines())

    loc, steps = "AAA", 0
    while loc != "ZZZ":
        loc = map[loc][next(directions)]
        steps += 1

    print(steps)
