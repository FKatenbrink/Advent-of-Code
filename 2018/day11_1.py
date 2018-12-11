import sys


def test_day11_1():
    assert day11_1("18") == ((33, 45), 29)
    assert day11_1("42") == ((21, 61), 30)
    assert power_level(3, 5, 8) == 4
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4
    print("All tests successful.")


def power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = int(str(power_level)[-3])
    power_level -= 5
    return power_level


def square_power_level(grid, x, y):
    if x > 298 or y > 298:
        return -sys.maxsize
    return sum(
        [grid[(xi, yi)] for xi in range(x, x + 3) for yi in range(y, y + 3)])


def day11_1(input):
    serial_number = int(input)
    grid = {(x, y): power_level(x, y, serial_number) for x in range(1, 301)
            for y in range(1, 301)}
    cell = max(grid, key=lambda xy: square_power_level(grid, xy[0], xy[1]))
    total_power = square_power_level(grid, cell[0], cell[1])
    return (cell, total_power)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day11_1(file.read().strip())}")
    else:
        test_day11_1()
