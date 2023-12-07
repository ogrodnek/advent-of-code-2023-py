import re

def possible_wins(time: int, record: int):
    return sum([1 if travel > record else 0 for travel in [i * (time - i) for i in range(1, time + 1)]])

with open("input.txt") as f:
    def parseLine(line):
        return int("".join(re.compile(r"(\d+)").findall(line)))
    
    time, distance = parseLine(f.readline()), parseLine(f.readline())
    print(possible_wins(time, distance))
