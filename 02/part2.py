from dataclasses import dataclass
import re
import math

colors = ["red", "blue", "green"]


@dataclass
class Game:
    id: int
    reveals: list[dict[str, int]]

    @property
    def min_cubes(self) -> dict[str, int]:
        return {color: max(reveal.get(color, 1) for reveal in self.reveals) for color in colors}
    
    @property
    def power(self) -> int:
        return math.prod(self.min_cubes.values())

reveal_pattern = re.compile(r"(\d+) (\w+)")    

def parse_reveal(reveal: str) -> dict[str, int]:
    cubes = reveal_pattern.findall(reveal)
    return {color: int(count) for count, color in cubes}


def parse_line(line: str) -> Game:
    id, reveals = line.split(":")
    id = int(id.split(" ")[1])
    reveals = [parse_reveal(r) for r in reveals.split(";")]
    
    return Game(id, reveals)


with open("input.txt") as f:
    games = [parse_line(line )for line in  f.readlines()]
    print(sum([game.power for game in games]))

