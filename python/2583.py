import sys
from collections import deque

X, Y, N = map(int, sys.stdin.readline().split())

road = [[0]*X for _ in range(Y)]
check = [[0]*X for _ in range(Y)]

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]


def draw(x1, y1, x2, y2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            road[j][i] = 1


def bfs(check, j, i):
    c = 1
    check[j][i] = 1
    q = deque()
    q.append([j, i])
    while len(q) > 0:
        now_x = q[0][0]
        now_y = q[0][1]
        q.popleft()
        for p in range(4):
            next_x = now_x + move_x[p]
            next_y = now_y + move_y[p]
            if next_x >= 0 and next_x < Y and next_y >= 0 and next_y < X:
                if check[next_x][next_y] == 0 and road[next_x][next_y] == 0:
                    check[next_x][next_y] = 1
                    c += 1
                    q.append([next_x, next_y])
    return c


for i in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    draw(x1, y1, x2, y2)

count = []
for i in range(X):
    for j in range(Y):
        if check[j][i] == 0 and road[j][i] == 0:
            count.append(bfs(check, j, i))

count.sort()
print(len(count))
print(" ".join(map(str, count)))
