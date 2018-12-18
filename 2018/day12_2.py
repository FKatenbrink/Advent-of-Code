import sys


def test_day12_1():
    assert day12_1(
        "initial state: #..#.#..##......###...###\n\n...## => #\n..#.. => #\n.#... => #\n.#.#. => #\n.#.## => #\n.##.. => #\n.#### => #\n#.#.# => #\n#.### => #\n##.#. => #\n##.## => #\n###.. => #\n###.# => #\n####. => #",
        1) == (".....#...#....#.....#..#..#..#.......", 91)
    assert day12_1(
        "initial state: #..#.#..##......###...###\n\n...## => #\n..#.. => #\n.#... => #\n.#.#. => #\n.#.## => #\n.##.. => #\n.#### => #\n#.#.# => #\n#.### => #\n##.#. => #\n##.## => #\n###.. => #\n###.# => #\n####. => #",
        20
    ) == (
        "........#....##....#####...#######....#.#..##...................................",
        325)
    print("All tests successful.")


def sum_plants(plants, left_index):
    return sum([i - left_index for i, s in enumerate(plants) if s == "#"])


def parse_rule(rule):
    # #..#. => #
    return (rule[:5], rule[9])


def day12_1(input, generations):
    lines = input.split("\n")
    plants = lines[0][15:]
    left_index = 0
    rules = list(map(parse_rule, lines[2:]))

    for k in range(generations):
        if k % 1000 == 0:
            print(f"{k}:\n{plants}")
        if plants[:5] != ".....":
            plants = "....." + plants
            left_index += 5
        if plants[-5:] != ".....":
            plants += "....."

        new_plants = "".join(["."] * len(plants))
        for i in range(len(plants)):
            match = False
            for rule in rules:
                if plants[i:i + 5] == rule[0]:
                    match = True
                    new_plants = new_plants[:i + 2] + rule[1] + new_plants[i +
                                                                           3:]
                    break
            if not match:
                new_plants = new_plants[:i + 2] + "." + new_plants[i + 3:]

        plants = new_plants

    print(f"{k}:\n{plants}")
    print(f"left_index: {left_index}")
    left_index = plants.index("#")
    print(f"index: {left_index}")
    result = sum_plants(plants, left_index)
    return plants, result


# The first # appears on the index 50000000000 - 64 = 49999999936
# and the pattern is ##.##.##.##....##.##.##.##.##.##.##.##.##....##.##.##.##.##.##.##.##.##....##.##.##....##.##.##.##.##.##....##.##.##.##.##.##.##.##....##.##.##.##.##.##.##.##.##.##
# ==> sum(49999999936 + 49999999937 + 49999999939 + 49999999940 + ...)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            day12_1(file.read().strip(), 1000)
    else:
        test_day12_1()
