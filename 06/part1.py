import re
import math

def possible_wins(time: int, record: int):
    return sum([1 if travel > record else 0 for travel in [i * (time - i) for i in range(1, time + 1)]])

with open("input.txt") as f:
    def parseLine(line):
        return [int(d) for d in re.compile(r"(\d+)").findall(line)]
    
    times, distances = parseLine(f.readline()), parseLine(f.readline())
    print(math.prod([possible_wins(time, record) for time, record in zip(times, distances)]))
