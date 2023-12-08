import itertools
from typing import Iterator
import re
import math


def parse_directions(line: str) -> Iterator[Iterator[int]]:
    directions = [0 if c == "L" else 1 for c in list(line.strip())]
    while True:
        yield itertools.cycle(directions)

def parse_map(lines: list[str]) -> dict[str, tuple[str, str]]:
    map = {}
    pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    
    for line in lines:
        match = pattern.match(line)
        if match:
            map[match.group(1)] = (match.group(2), match.group(3))
        
    return map

def solve(start_loc: str, directions: Iterator[int], map: dict[str, tuple[str, str]]) -> int:
    loc, steps = start_loc, 0

    while not loc.endswith("Z"):
        loc = map[loc][next(directions)]
        steps += 1

    return steps

with open("input.txt") as f:
    directions = parse_directions(f.readline())
    f.readline()
    map = parse_map(f.readlines())

    locations = [k for k in map.keys() if k.endswith("A")]
    steps = [solve(loc, next(directions), map) for loc in locations]
    print(math.lcm(*steps))
