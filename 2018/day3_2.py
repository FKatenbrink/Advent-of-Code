import sys
import re


def test_day3_2():
    assert day3_2("#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2") == 3
    print("All tests successful.")


class Claim:

    def __init__(self, id, x, y, width, height):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def parse_claim(line):
    # #1 @ 1,3: 4x4
    regex = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
    match = re.search(regex, line)
    id = int(match.group(1))
    x = int(match.group(2))
    y = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))
    return Claim(id, x, y, width, height)


def claim_fabric(claim, fabric):
    for i in range(claim.height):
        for j in range(claim.width):
            if fabric[i + claim.y][j + claim.x] == 0:
                fabric[i + claim.y][j + claim.x] = claim.id
            else:
                fabric[i + claim.y][j + claim.x] = -1
    return fabric


def has_claim_overlap(claim, fabric):
    for i in range(claim.height):
        for j in range(claim.width):
            if fabric[i + claim.y][j + claim.x] != claim.id:
                return True
    return False


def day3_2(input):
    lines = input.split("\n")
    claims = [parse_claim(line) for line in lines]
    fabric_width = max([c.x + c.width for c in claims])
    fabric_height = max([c.y + c.height for c in claims])
    fabric = [[0 for x in range(fabric_width)] for y in range(fabric_height)]
    for c in claims:
        fabric = claim_fabric(c, fabric)
    for c in claims:
        if not has_claim_overlap(c, fabric):
            return c.id


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day3_2(file.read().strip())}")
    else:
        test_day3_2()
