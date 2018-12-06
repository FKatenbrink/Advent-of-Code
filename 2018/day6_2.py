import sys
import re


def test_day6_2():
    assert line_to_point("350, 353") == (350, 353)
    assert day6_2("1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9") == 16
    print("All tests successful.")


def line_to_point(line):
    # 350, 353
    regex = r"(\d+), (\d+)"
    match = re.search(regex, line)
    x = int(match.group(1))
    y = int(match.group(2))
    return (x, y)


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def day6_2(input):
    lines = input.split("\n")
    points = [line_to_point(line) for line in lines]
    width = max([c[0] for c in points]) + 1
    height = max([c[1] for c in points]) + 1
    grid = {(x, y): 0 for x in range(width) for y in range(height)}

    for k, v in grid.items():
        for coord in points:
            grid[k] += manhattan_distance(k, coord)

    return len([k for k in grid if grid[k] < 10000])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day6_2(file.read().strip())}")
    else:
        test_day6_2()
