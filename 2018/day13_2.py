import sys


def test_day13_2():
    assert day13_2(
        "/>-<\\  \n|   |  \n| /<+-\\\n| | | v\n\\>+</ |\n  |   ^\n  \\<->/",
        5) == (4, (6, 4))
    print("All tests successful.")


direction = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}
new_direction = {
    ("<", "<"): "<",
    ("<", "-"): "<",
    ("<", "/"): "v",
    ("<", "\\"): "^",
    (">", ">"): ">",
    (">", "-"): ">",
    (">", "/"): "^",
    (">", "\\"): "v",
    ("^", "^"): "^",
    ("^", "|"): "^",
    ("^", "/"): ">",
    ("^", "\\"): "<",
    ("v", "v"): "v",
    ("v", "|"): "v",
    ("v", "/"): "<",
    ("v", "\\"): ">"
}
new_intersection_direction = {
    ("<", "left"): ("<", "straight"),
    ("<", "straight"): ("^", "right"),
    ("<", "right"): ("v", "left"),
    (">", "left"): (">", "straight"),
    (">", "straight"): ("v", "right"),
    (">", "right"): ("^", "left"),
    ("^", "left"): ("^", "straight"),
    ("^", "straight"): (">", "right"),
    ("^", "right"): ("<", "left"),
    ("v", "left"): ("v", "straight"),
    ("v", "straight"): ("<", "right"),
    ("v", "right"): (">", "left")
}


def move(cart, mine):
    x, y, d, i = cart
    x += direction[d][0]
    y += direction[d][1]
    if mine[y][x] == "+":
        d, i = new_intersection_direction[(d, i)]
    elif (d, mine[y][x]) in new_direction:
        d = new_direction[(d, mine[y][x])]

    return (x, y, d, i)


def collided(carts):
    coords = {}
    for idx, cart in enumerate(carts):
        x, y, d, i = cart
        c = (x, y)
        if c in coords:
            return (coords[c], idx)
        else:
            coords[c] = idx

    return None


def print_mine(mine):
    rows = ["".join(m) for m in mine]
    print("\n".join(rows))


def strtolist(s):
    return [c for c in s]


def day13_2(input, generations):
    mine = [strtolist(line) for line in input.splitlines()]
    width, height = len(mine[0]), len(mine)
    carts = [(x, y, mine[y][x], "right")
             for x in range(width)
             for y in range(height)
             if mine[y][x] in direction]

    for t in range(1, generations):
        if len(carts) == 1:
            return (t, carts[0][0:2])

        i = 0
        while i < len(carts):
            c = carts[i]
            carts[i] = move(c, mine)
            collision = collided(carts)
            if collision:
                # mine[collision[1]][collision[0]] = "X"
                # print_mine(mine)
                del carts[collision[0]]
                del carts[collision[1] - 1]
                if collision[0] <= i:
                    i -= 1
                if collision[1] - 1 <= i:
                    i -= 1
            i += 1
        carts = sorted(carts, key=lambda c: (c[1], c[0]))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(
                f"Result for file input: {format(day13_2(file.read(), 200000))}"
            )
    else:
        test_day13_2()
