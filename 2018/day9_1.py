import sys
import re


def test_day9_1():
    result = day9_1("9 players; last marble is worth 25 points")
    assert result == (5, 32), "Result: " + str(result)
    result = day9_1("10 players; last marble is worth 1618 points")
    assert result[1] == 8317, "Result: " + str(result)
    result = day9_1("13 players; last marble is worth 7999 points")
    assert result[1] == 146373, "Result: " + str(result)
    result = day9_1("17 players; last marble is worth 1104 points")
    assert result[1] == 2764, "Result: " + str(result)
    result = day9_1("21 players; last marble is worth 6111 points")
    assert result[1] == 54718, "Result: " + str(result)
    result = day9_1("30 players; last marble is worth 5807 points")
    assert result[1] == 37305, "Result: " + str(result)
    print("All tests successful.")


def parse_input(input):
    # 10 players; last marble is worth 1618 points
    regex = r"(\d+) players; last marble is worth (\d+) points"
    match = re.search(regex, input)
    players = int(match.group(1))
    rounds = int(match.group(2))
    return (players, rounds)


def day9_1(input):
    players, rounds = parse_input(input)
    points = [0] * players
    circle = [0]
    current_marble_idx = 0
    current_player_idx = 0
    for value in range(1, rounds + 1):
        if value % 23 == 0:
            points[current_player_idx] += value
            current_marble_idx = (current_marble_idx - 7) % len(circle)
            points[current_player_idx] += circle.pop(current_marble_idx)
        else:
            current_marble_idx = (current_marble_idx + 1) % len(circle) + 1
            circle.insert(current_marble_idx, value)
        current_player_idx = (current_player_idx + 1) % players

    highscore = max(points)
    winner = points.index(highscore) + 1
    return (winner, highscore)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day9_1(file.read().strip())}")
    else:
        test_day9_1()
