import sys


def test_day14_1():
    assert day14_1(9) == "5158916779"
    assert day14_1(5) == "0124515891"
    assert day14_1(18) == "9251071085"
    assert day14_1(2018) == "5941429882"
    print("All tests successful.")


def day14_1(input):
    recipes_after = int(input)
    total_recipes = recipes_after + 10
    recipes = [3, 7]
    elves = [0, 1]
    while len(recipes) < total_recipes:
        sum = recipes[elves[0]] + recipes[elves[1]]
        recipes += [int(d) for d in str(sum)]
        elves[0] = (elves[0] + 1 + recipes[elves[0]]) % len(recipes)
        elves[1] = (elves[1] + 1 + recipes[elves[1]]) % len(recipes)

    result = "".join(map(str, recipes[recipes_after:recipes_after + 10]))
    return result


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(
                f"Result for file input: {format(day14_1(file.read().strip()))}"
            )
    else:
        test_day14_1()
