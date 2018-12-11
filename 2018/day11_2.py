import sys


def test_day11_2():
    assert day11_2("18") == ((90, 269, 16), 113)
    print("18 test successful.")
    assert day11_2("42") == ((232, 251, 12), 119)
    print("42 test successful.")
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


def square_power_level(grid, x, y, size):
    if x + size > 301 or y + size > 301:
        return -sys.maxsize
    return sum([
        grid[(xi, yi)]
        for xi in range(x, x + size)
        for yi in range(y, y + size)
    ])


def day11_2(input):
    serial_number = int(input)
    grid = {(x, y): power_level(x, y, serial_number) for x in range(1, 301)
            for y in range(1, 301)}

    max_cell = (1, 1, 1)
    max_power = grid[(1, 1)]
    for x in range(1, 301):
        print(f"x: {x}")
        for y in range(1, 301):
            # print(f"y: {y}")
            for size in range(1, 51):
                power = square_power_level(grid, x, y, size)
                if power > max_power:
                    max_cell = (x, y, size)
                    max_power = power

    return (max_cell, max_power)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day11_2(file.read().strip())}")
    else:
        test_day11_2()
