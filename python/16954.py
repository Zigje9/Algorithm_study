import sys

chess = []
for _ in range(8):
    chess.append(list(map(str, sys.stdin.readline().rstrip())))

move_x = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
move_y = [-1, 0, 1, 1, 1, 0, -1, -1, 0]


def down():
    for k in range(8):
        if chess[7][k] == "#":
            chess[7][k] = "."
    for i in range(6, -1, -1):
        for j in range(8):
            if chess[i][j] == "#":
                chess[i][j] = "."
                chess[i+1][j] = "#"


def bfs(position):
    temp = []
    for x, y in position:
        for i in range(9):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if 0 <= next_x < 8 and 0 <= next_y < 8:
                if chess[next_x][next_y] == ".":
                    if [next_x, next_y] not in temp:
                        temp.append([next_x, next_y])

    return temp


def delete(position):
    delete_position = []
    for x, y in position:
        if chess[x][y] == ".":
            delete_position.append([x, y])

    return delete_position


flag = True
count = 1
position = []
position.append([7, 0])
next_position = bfs(position)
down()
next_position = delete(next_position)
while True:
    if count == 9:
        break

    if len(next_position) == 0:
        flag = False
        break

    bfs_position = bfs(next_position)
    down()
    next_position = delete(bfs_position)

    count += 1

if flag:
    print(1)
else:
    print(0)
