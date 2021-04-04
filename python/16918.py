import sys
from collections import deque

R, C, T = map(int, sys.stdin.readline().split())

bomberman = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

bomb_location = deque()


def make_list():
    for x in range(R):
        for y in range(C):
            if bomberman[x][y] == "O":
                bomb_location.append([x, y])


def set_bomb():
    for x in range(R):
        for y in range(C):
            if bomberman[x][y] == ".":
                bomberman[x][y] = "O"


def bomb():
    while bomb_location:
        now_x, now_y = bomb_location.popleft()
        bomberman[now_x][now_y] = "."
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < R and 0 <= next_y < C:
                bomberman[next_x][next_y] = "."


N = 2
while N <= T:
    if N % 2 == 0:
        make_list()
        set_bomb()
    else:
        bomb()
        make_list()
    N += 1

for i in range(R):
    print("".join(bomberman[i]))
