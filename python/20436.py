import sys

left_keyboard = {
    "z": (0, 0),
    "x": (1, 0),
    "c": (2, 0),
    "v": (3, 0),
    "a": (0, 1),
    "s": (1, 1),
    "d": (2, 1),
    "f": (3, 1),
    "g": (4, 1),
    "q": (0, 2),
    "w": (1, 2),
    "e": (2, 2),
    "r": (3, 2),
    "t": (4, 2)
}

right_keyboard = {
    "b": (4, 0),
    "n": (5, 0),
    "m": (6, 0),
    "h": (5, 1),
    "j": (6, 1),
    "k": (7, 1),
    "l": (8, 1),
    "y": (5, 2),
    "u": (6, 2),
    "i": (7, 2),
    "o": (8, 2),
    "p": (9, 2)
}

now_left, now_right = map(str, sys.stdin.readline().split())

word = str(sys.stdin.readline().rstrip())

time = 0

for w in word:
    if w in left_keyboard:
        now_x, now_y = left_keyboard[now_left][0], left_keyboard[now_left][1]
        next_x, next_y = left_keyboard[w][0], left_keyboard[w][1]
        time += (abs(next_x-now_x) + abs(next_y-now_y))
        now_left = w
        time += 1
    else:
        now_x, now_y = right_keyboard[now_right][0], right_keyboard[now_right][1]
        next_x, next_y = right_keyboard[w][0], right_keyboard[w][1]
        time += (abs(next_x-now_x) + abs(next_y-now_y))
        now_right = w
        time += 1

print(time)
