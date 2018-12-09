import sys
import re


def parse_input(input):
    # 10 players; last marble is worth 1618 points
    regex = r"(\d+) players; last marble is worth (\d+) points"
    match = re.search(regex, input)
    players = int(match.group(1))
    rounds = int(match.group(2)) * 100
    return (players, rounds)


def day9_2(input):
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
        if value % 100000 == 0:
            print(value)

    highscore = max(points)
    winner = points.index(highscore) + 1
    return (winner, highscore)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day9_2(file.read().strip())}")
