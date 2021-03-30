import sys

N = int(sys.stdin.readline())

find_num = int(sys.stdin.readline())

snail = [[0]*N for _ in range(N)]

x = 0
y = 0
direction = "down"
value = N*N
while True:
    if snail[x][y] == 0:
        snail[x][y] = value
        if value == find_num:
            find_x, find_y = x+1, y+1
        value -= 1

    if value == 0:
        break

    if direction == "down":
        if 0 <= x+1 and x+1 <= N-1:
            if snail[x+1][y] != 0:
                direction = "right"
            else:
                x = x+1
        else:
            direction = "right"
    elif direction == "right":
        if 0 <= y+1 and y+1 <= N-1:
            if snail[x][y+1] != 0:
                direction = "up"
            else:
                y = y+1
        else:
            direction = "up"
    elif direction == "left":
        if 0 <= y-1 and y-1 <= N-1:
            if snail[x][y-1] != 0:
                direction = "down"
            else:
                y = y-1
        else:
            direction = "down"
    else:
        if 0 <= x-1 and x-1 <= N-1:
            if snail[x-1][y] != 0:
                direction = "left"
            else:
                x = x-1
        else:
            direction = "left"

for i in range(N):
    print(" ".join(map(str, snail[i])))
print(find_x, find_y)
