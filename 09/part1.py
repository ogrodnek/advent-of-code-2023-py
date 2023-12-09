Tree = list[list[int]]

def next_line(line: list[int]) -> list[int]:
    return [line[i + 1] - num for i, num in enumerate(line[:-1])]

def parse_tree(tree: Tree) -> Tree:
    line = next_line(tree[-1])
    if all([num == 0 for num in line]):
        return tree
    return parse_tree(tree + [line])


def parse_line(line: str) -> Tree:
    nums = [int(d) for d in line.strip().split()]
    return parse_tree([nums])

def next_val(tree: Tree) -> int:
    return sum([line[-1] for line in tree])

with open("input.txt") as f:
    lines = f.readlines()

    vals = [next_val(parse_line(line)) for line in lines]
    print(sum(vals))

