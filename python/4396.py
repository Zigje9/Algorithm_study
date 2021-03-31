import sys

N = int(sys.stdin.readline())

hide = []

hide.append(["."]*(N+2))
for _ in range(N):
    hide.append(["."]+list(map(str, sys.stdin.readline().rstrip()))+["."])
hide.append(["."]*(N+2))

game = []

for _ in range(N):
    game.append(list(map(str, sys.stdin.readline().rstrip())))

move_x = [-1, -1, -1, 0, 1, 1, 1, 0]
move_y = [-1, 0, 1, 1, 1, 0, -1, -1]


def find(x, y):
    if hide[x][y] == "*":
        return -1

    result = 0

    for i in range(8):
        if hide[x+move_x[i]][y+move_y[i]] == "*":
            result += 1

    return result


def change_bomb():
    for i in range(N):
        for j in range(N):
            if hide[i+1][j+1] == "*":
                game[i][j] = "*"


for i in range(N):
    for j in range(N):
        if game[i][j] == "x":
            num = find(i+1, j+1)
            if num == -1:
                change_bomb()
            else:
                game[i][j] = num

for i in range(N):
    print("".join(map(str, game[i])))
