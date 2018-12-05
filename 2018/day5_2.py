import sys
import string


def test_day2_1():
    assert day2_1("dabAcCaCBAcCcaDA") == 10
    assert day2_1("abBA") == 0
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


def remove_letters(polymer, letter):
    return list(
        filter(lambda k: k != letter.lower() and k != letter.upper(), polymer))


def day2_1(input):
    polymer = list(input)
    old_len_polymer = len(polymer)
    alphabet = list(string.ascii_lowercase)
    min = len(polymer)
    for letter in alphabet:
        new_polymer = remove_letters(polymer, letter)
        while True:
            new_polymer = react(new_polymer)
            if len(new_polymer) == old_len_polymer:
                if old_len_polymer < min:
                    min = old_len_polymer
                break
            else:
                old_len_polymer = len(new_polymer)
    return min


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day2_1(file.read().strip())}")
    else:
        test_day2_1()
