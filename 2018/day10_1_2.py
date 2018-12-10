import sys
import re


def test_day9_1():
    day9_1(
        "position=< 9,  1> velocity=< 0,  2>\nposition=< 7,  0> velocity=<-1,  0>\nposition=< 3, -2> velocity=<-1,  1>\nposition=< 6, 10> velocity=<-2, -1>\nposition=< 2, -4> velocity=< 2,  2>\nposition=<-6, 10> velocity=< 2, -2>\nposition=< 1,  8> velocity=< 1, -1>\nposition=< 1,  7> velocity=< 1,  0>\nposition=<-3, 11> velocity=< 1, -2>\nposition=< 7,  6> velocity=<-1, -1>\nposition=<-2,  3> velocity=< 1,  0>\nposition=<-4,  3> velocity=< 2,  0>\nposition=<10, -3> velocity=<-1,  1>\nposition=< 5, 11> velocity=< 1, -2>\nposition=< 4,  7> velocity=< 0, -1>\nposition=< 8, -2> velocity=< 0,  1>\nposition=<15,  0> velocity=<-2,  0>\nposition=< 1,  6> velocity=< 1,  0>\nposition=< 8,  9> velocity=< 0, -1>\nposition=< 3,  3> velocity=<-1,  1>\nposition=< 0,  5> velocity=< 0, -1>\nposition=<-2,  2> velocity=< 2,  0>\nposition=< 5, -2> velocity=< 1,  2>\nposition=< 1,  4> velocity=< 2,  1>\nposition=<-2,  7> velocity=< 2, -2>\nposition=< 3,  6> velocity=<-1, -1>\nposition=< 5,  0> velocity=< 1,  0>\nposition=<-6,  0> velocity=< 2,  0>\nposition=< 5,  9> velocity=< 1, -2>\nposition=<14,  7> velocity=<-2,  0>\nposition=<-3,  6> velocity=< 2, -1>",
        3)


def parse_input(input):
    # position=<-4,  3> velocity=< 2,  0>
    # position=<15,  0> velocity=<-2,  0>
    regex = r"position=<\s*(-?)(\d+),\s*(-?)(\d+)> velocity=<\s*(-?)(\d+),\s*(-?)(\d+)>"
    match = re.search(regex, input)
    x = int(match.group(2))
    if match.group(1):
        x = -x
    y = int(match.group(4))
    if match.group(3):
        y = -y
    x_velocity = int(match.group(6))
    if match.group(5):
        x_velocity = -x_velocity
    y_velocity = int(match.group(8))
    if match.group(7):
        y_velocity = -y_velocity
    return (x, y, x_velocity, y_velocity)


def print_image(points):
    image = empty_image(points)
    for p in points:
        image[p[1]][p[0]] = "#"
    rows = ["".join(chars) for chars in image]
    print("\n".join(rows))


def move_points(points):
    return [(p[0] + p[2],) + (p[1] + p[3],) + p[2:] for p in points]


def empty_image(points):
    return [["."
             for _ in range(max([p1[0]
                                 for p1 in points]) + 1)]
            for _ in range(max([p2[1] for p2 in points]) + 1)]


def shift_points(points):
    min_width = min([p[0] for p in points])
    if min_width < 0:
        points = [(p[0] - min_width,) + p[1:] for p in points]
    min_height = min([p[1] for p in points])
    if min_height < 0:
        points = [(p[0],) + (p[1] - min_height,) + p[2:] for p in points]
    return points


def day9_1(input, seconds=100):
    points = [parse_input(i) for i in input.split("\n")]
    seconds = 0
    while True:
        points = move_points(points)
        max_height = max([p[1] for p in points])
        min_height = min([p[1] for p in points])
        seconds += 1
        if max_height - min_height == 9:
            break

    print(f"Seconds {seconds}:")
    print_image(points)
    points = move_points(points)
    points = shift_points(points)
    return seconds


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day9_1(file.read().strip())}")
    else:
        test_day9_1()
