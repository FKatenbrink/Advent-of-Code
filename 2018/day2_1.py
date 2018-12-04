import sys
from collections import defaultdict


def test_day2_1():
    assert evaluate_line("abcdef") == (0, 0)
    assert evaluate_line("bababc") == (1, 1)
    assert evaluate_line("abbcde") == (1, 0)
    assert evaluate_line("abcccd") == (0, 1)
    assert evaluate_line("aabcdd") == (1, 0)
    assert evaluate_line("abcdee") == (1, 0)
    assert evaluate_line("ababab") == (0, 1)
    assert day2_1(
        "abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab") is 12
    print("All tests successful.")


def evaluate_line(line):
    characters = defaultdict(int)
    for c in line:
        characters[c] += 1
    two = 0
    three = 0
    for _, val in characters.items():
        if val is 2:
            two = 1
        if val is 3:
            three = 1
    return (two, three)


def day2_1(input):
    line_values = [evaluate_line(line) for line in input.split("\n")]
    twos = sum([two for (two, _) in line_values])
    threes = sum([three for (_, three) in line_values])
    return twos * threes


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day2_1(file.read().strip())}")
    else:
        test_day2_1()
