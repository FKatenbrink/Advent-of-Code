import sys
import re


def test_day3_1():
    assert day3_1("#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2") == 4
    print("All tests successful.")


class Claim:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def parse_claim(line):
    # #1 @ 1,3: 4x4
    regex = r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)"
    match = re.search(regex, line)
    x = int(match.group(1))
    y = int(match.group(2))
    width = int(match.group(3))
    height = int(match.group(4))
    return Claim(x, y, width, height)


def claim_fabric(claim, fabric):
    for i in range(claim.height):
        for j in range(claim.width):
            fabric[i + claim.y][j + claim.x] += 1
    return fabric


def day3_1(input):
    lines = input.split("\n")
    claims = [parse_claim(line) for line in lines]
    fabric_width = max([c.x + c.width for c in claims])
    fabric_height = max([c.y + c.height for c in claims])
    fabric = [[0 for x in range(fabric_width)] for y in range(fabric_height)]
    for c in claims:
        fabric = claim_fabric(c, fabric)

    multiple_fabric = [
        list(map(lambda n: 1 if n > 1 else 0, fabric_col))
        for fabric_col in fabric
    ]
    return sum(list(map(sum, multiple_fabric)))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day3_1(file.read().strip())}")
    else:
        test_day3_1()
