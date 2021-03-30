import sys

bingo = []
for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))

call = []
for _ in range(5):
    call += list(map(int, sys.stdin.readline().split()))


def check_row():
    result = 0
    for i in range(5):
        if sum(bingo[i]) == 0:
            result += 1
    return result


def check_col():
    result = 0
    for i in range(5):
        flag = True
        for j in range(5):
            if bingo[j][i] != 0:
                flag = False
                break
        if flag:
            result += 1
    return result


def check_dia():
    result = 0
    if bingo[2][2] != 0:
        return 0
    if bingo[0][0] + bingo[1][1] + bingo[3][3] + bingo[4][4] == 0:
        result += 1
    if bingo[0][4] + bingo[1][3] + bingo[3][1] + bingo[4][0] == 0:
        result += 1
    return result


for idx, value in enumerate(call):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == value:
                bingo[i][j] = 0
                break
    if idx >= 11:
        if check_col() + check_dia() + check_row() >= 3:
            print(idx+1)
            sys.exit()
