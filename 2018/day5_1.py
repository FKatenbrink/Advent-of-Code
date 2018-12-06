import sys


def test_day5_1():
    assert day5_1("dabAcCaCBAcCcaDA") == 10
    assert day5_1("abBA") == 0
    assert react(["a", "A"]) == []
    assert react(["a", "B", "b", "A"]) == ["a", "A"]
    print("All tests successful.")


def can_react(unit1, unit2):
    return (unit1 == unit2.upper() and
            unit1.lower() == unit2) or (unit1.upper() == unit2 and
                                        unit1 == unit2.lower())


def react(polymer):
    for i in range(len(polymer) - 1):
        if can_react(polymer[i], polymer[i + 1]):
            del polymer[i:i + 2]
            break
    return polymer


def day5_1(input):
    polymer = list(input)
    old_len_polymer = len(polymer)
    while True:
        polymer = react(polymer)
        if len(polymer) == old_len_polymer:
            return old_len_polymer
        else:
            old_len_polymer = len(polymer)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day5_1(file.read().strip())}")
    else:
        test_day5_1()
