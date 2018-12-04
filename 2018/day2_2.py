import sys


def test_day2_2():
    assert compare("fghij", "fguij") == "fgij"
    assert day2_2("abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz") == "fgij"
    print("All tests successful.")


def compare(line1, line2):
    assert len(line1) == len(line2)
    common_letters = 0
    difference_index = -1
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            common_letters += 1
        else:
            difference_index = i
    if len(line1) - common_letters == 1:
        return line1[:difference_index] + line1[difference_index + 1:]


def day2_2(input):
    lines = input.split("\n")
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            diff = compare(lines[i], lines[j])
            if diff:
                return diff


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day2_2(file.read().strip())}")
    else:
        test_day2_2()
