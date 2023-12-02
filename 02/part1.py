from dataclasses import dataclass
import re


max_cube_counts = {
    "red": 12,
    "blue": 14,
    "green": 13,
}

@dataclass
class Game:
    id: int
    reveals: list[dict[str, int]]

    @property
    def possible(self) -> bool:
        def reveal_possible(reveal: dict[str, int]) -> bool:
            return all(reveal[color] <= max_cube_counts[color] for color in reveal)
        
        return all(reveal_possible(reveal) for reveal in self.reveals)



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
    print(sum([game.id for game in games if game.possible]))

