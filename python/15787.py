import sys

N, M = map(int, sys.stdin.readline().split())

all_train = [["X" for _ in range(22)] for _ in range(N)]


def command1(i, x):
    all_train[i][x] = "O"


def command2(i, x):
    all_train[i][x] = "X"


def command3(i):
    for j in range(20, 0, -1):
        if all_train[i][j] == "O":
            all_train[i][j] = "X"
            all_train[i][j+1] = "O"


def command4(i):
    for j in range(1, 21):
        if all_train[i][j] == "O":
            all_train[i][j] = "X"
            all_train[i][j-1] = "O"


for _ in range(M):
    c = list(map(int, sys.stdin.readline().split()))
    if c[0] == 1:
        command1(c[1]-1, c[2])
    elif c[0] == 2:
        command2(c[1]-1, c[2])
    elif c[0] == 3:
        command3(c[1]-1)
    else:
        command4(c[1]-1)

answer = []
for i in range(N):
    answer.append("".join(all_train[i][1:-1]))

print(len(set(answer)))
