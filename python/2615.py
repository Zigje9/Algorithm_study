import sys

go = []

for _ in range(19):
    go.append(list(map(int, sys.stdin.readline().split())))


def check_row(alpha, x, y):
    for i in range(1, 5):
        if alpha != go[x][y+i]:
            return False
    if y != 14:
        if alpha == go[x][y+5]:
            return False
    if y != 0:
        if alpha == go[x][y-1]:
            return False
    return True


def check_col(alpha, x, y):
    for i in range(1, 5):
        if alpha != go[x+i][y]:
            return False
    if x != 14:
        if alpha == go[x+5][y]:
            return False
    if x != 0:
        if alpha == go[x-1][y]:
            return False
    return True


def check_left_dia(alpha, x, y):
    for i in range(1, 5):
        if alpha != go[x-i][y+i]:
            return False
    if x != 4 and y != 14:
        if alpha == go[x-5][y+5]:
            return False
    if x != 14 and y != 0:
        if alpha == go[x+1][y-1]:
            return False
    return True


def check_right_dia(alpha, x, y):
    for i in range(1, 5):
        if alpha != go[x+i][y+i]:
            return False
    if x != 14 and y != 14:
        if alpha == go[x+5][y+5]:
            return False
    if x != 0 and y != 0:
        if alpha == go[x-1][y-1]:
            return False
    return True


for i in range(19):
    for j in range(15):
        if go[i][j] != 0:
            if check_row(go[i][j], i, j):
                print(go[i][j])
                print(i+1, j+1)
                sys.exit()

for i in range(15):
    for j in range(19):
        if go[i][j] != 0:
            if check_col(go[i][j], i, j):
                print(go[i][j])
                print(i+1, j+1)
                sys.exit()

for i in range(4, 19):
    for j in range(15):
        if go[i][j] != 0:
            if check_left_dia(go[i][j], i, j):
                print(go[i][j])
                print(i+1, j+1)
                sys.exit()

for i in range(15):
    for j in range(15):
        if go[i][j] != 0:
            if check_right_dia(go[i][j], i, j):
                print(go[i][j])
                print(i+1, j+1)
                sys.exit()

print(0)
