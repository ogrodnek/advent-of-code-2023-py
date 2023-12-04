def score_card(winning: set[str], hand: set[str]) -> int:
    won = len(winning.intersection(hand))

    return 0 if won == 0 else 2 ** (won - 1)

def parse_card(line: str) -> tuple[set[str], set[str]]:
    a, b = line.split(":")[1].strip().split("|")
    return set(a.split()), set(b.split())


with open("input.txt") as f:
    cards = [parse_card(line) for line in f.readlines()]
    print(sum([score_card(a, b) for a, b in cards]))
