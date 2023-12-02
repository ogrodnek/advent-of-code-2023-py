import re

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

pattern = re.compile(r"(?=([1-9]|" + "|".join(numbers.keys()) + "))")

def get_calibration(line: str) -> int:
    digits = [numbers.get(d, d) for d in pattern.findall(line)]
    return int(digits[0] + digits[-1])

with open("input.txt") as f:
    print(sum([get_calibration(line) for line in f.readlines()]))
