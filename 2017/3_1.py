# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49 ...

# Total:      1,  8, 16, 24, 32
# Side length: 1,  3,  5,  7,  9

# Formula: 4*x + 4 <= 312051

import sys
import math


def test_day_3_1():
    assert day_3_1(1) is 0
    assert day_3_1(12) is 3
    assert day_3_1(23) is 2
    assert day_3_1(41) is 4
    assert day_3_1(15) is 2
    assert day_3_1(23) is 2
    assert day_3_1(1024) is 31


def day_3_1(input):
    # Calculate sqrt of largest number in layer (bottom-right corner)
    # This is the length of each side
    # Round up to the next uneven number
    len_side = math.ceil(math.sqrt(int(input)))
    if len_side % 2 == 0:
        len_side += 1
    # Largest number in the layer (bottom-right corner)
    lower_corner = math.pow(len_side, 2)

    def manhattan_distance(corner):
        center_dist = abs(input - (corner + int(len_side/2)))
        return int(center_dist + len_side/2)

    def rotate_clockwise(corner):
        return corner - (len_side - 1)

    # Rotate clockwise 4 times
    for i in range(4):
        lower_corner = rotate_clockwise(lower_corner)
        if input >= lower_corner:
            return manhattan_distance(lower_corner)
    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(day_3_1(int(sys.argv[1])))
    else:
        test_day_3_1()
