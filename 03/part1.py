import re
from dataclasses import dataclass
from typing import Iterator

symbol_chars= {'%', '@', '=', '&', '/', '*', '-', '$', '+', '#'}

def is_symbol(char: str) -> bool:
    return char in symbol_chars


@dataclass
class PartNo:
    grid: list[list[str]]
    row: int
    start_col: int
    end_col: int
    val: int

    @property
    def surrounding_chars(self) -> Iterator[str]:
        def chars_in_row(row: int) -> list[str]:
            search_range = range(max(0, self.start_col -1), min(len(self.grid[self.row]) - 1, self.end_col + 2))
            return [self.grid[row][col] for col in search_range]
            
        if self.row > 0:
            yield from chars_in_row(self.row - 1)
        if self.row < len(self.grid) - 1:
            yield from chars_in_row(self.row + 1)

        if self.start_col > 0:
            yield self.grid[self.row][self.start_col - 1]
        
        if self.end_col < len(self.grid[self.row]) - 1:
            yield self.grid[self.row][self.end_col + 1]
        
    @property
    def is_valid(self):
        return any((is_symbol(char) for char in self.surrounding_chars))


def parse_parts(grid: list[list[str]]) -> Iterator[PartNo]:
    pattern = re.compile(r"(\d+)")
    for row, line in enumerate(grid):
        for match in pattern.finditer("".join(line)):
            yield PartNo(grid, row, match.start(), match.end() - 1, int(match.group(1)))
            
with open("input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]
    print(sum([part.val for part in parse_parts(grid) if part.is_valid]))
