import sys


def test_day14_1():
    assert day14_1("51589") == 9
    assert day14_1("01245") == 5
    assert day14_1("92510") == 18
    assert day14_1("59414") == 2018
    print("All tests successful.")


def day14_1(input):
    target_recipe = list(map(int, list(input)))
    recipes = [3, 7]
    elves = [0, 1]
    found = False
    while True:
        sum = recipes[elves[0]] + recipes[elves[1]]
        for d in str(sum):
            recipes += [int(d)]
            if recipes[-len(target_recipe):] == target_recipe:
                found = True
                break

        if found:
            return len(recipes) - len(target_recipe)

        elves[0] = (elves[0] + 1 + recipes[elves[0]]) % len(recipes)
        elves[1] = (elves[1] + 1 + recipes[elves[1]]) % len(recipes)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(
                f"Result for file input: {format(day14_1(file.read().strip()))}"
            )
    else:
        test_day14_1()
