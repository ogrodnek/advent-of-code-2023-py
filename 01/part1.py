def get_calibration(line: str) -> int:
    digits = [d for d in line if d.isdigit()]
    return int(digits[0] + digits[-1])

with open("input.txt") as f:
    print(sum([get_calibration(line) for line in f.readlines()]))
