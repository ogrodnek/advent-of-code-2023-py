import re
from dataclasses import dataclass
from typing import Iterator

def is_gear(char: str) -> bool:
    return "*" == char

@dataclass(eq=True, frozen=True)
class Gear:
    row: int
    col: int

@dataclass
class PartNo:
    grid: list[list[str]]
    row: int
    start_col: int
    end_col: int
    val: int

    @property
    def surrounding_chars(self) -> Iterator[tuple[int, int, str]]:
        def chars_in_row(row: int) -> list[tuple[int, int, str]]:
            search_range = range(max(0, self.start_col -1), min(len(self.grid[self.row]) - 1, self.end_col + 2))
            return [(row, col, self.grid[row][col]) for col in search_range]
            
        if self.row > 0:
            yield from chars_in_row(self.row - 1)
        if self.row < len(self.grid) - 1:
            yield from chars_in_row(self.row + 1)

        if self.start_col > 0:
            yield (self.row, self.start_col - 1, self.grid[self.row][self.start_col - 1])
        
        if self.end_col < len(self.grid[self.row]) - 1:
            yield (self.row, self.end_col + 1, self.grid[self.row][self.end_col + 1])

    @property
    def gears(self) -> Iterator[Gear]:
        return (Gear(row, col) for row, col, char in self.surrounding_chars if is_gear(char))


@dataclass
class GearSet:
    gear: Gear
    parts: list[int]

    @property
    def ratio(self):
        return self.parts[0] * self.parts[1]


def parse_parts(grid: list[list[str]]) -> list[PartNo]:
    pattern = re.compile(r"(\d+)")
    for row, line in enumerate(grid):
        for match in pattern.finditer("".join(line)):
            yield PartNo(grid, row, match.start(), match.end() - 1, int(match.group(1)))

def match_gear_sets(parts: list[PartNo]) -> list[GearSet]:
    gear_sets = {}
    for part in parts:
        for gear in part.gears:
            if gear not in gear_sets:
                gear_sets[gear] = GearSet(gear, [])
            gear_sets[gear].parts.append(part.val)
    
    return [gear_set for gear_set in gear_sets.values() if len(gear_set.parts) > 1]

            
with open("input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]
    parts = [part for part in parse_parts(grid)]

    print(sum([gear_set.ratio for gear_set in match_gear_sets(parts)]))
