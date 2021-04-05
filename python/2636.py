import sys
from collections import deque

X, Y = map(int, sys.stdin.readline().split())

cheeze = [list(map(int, sys.stdin.readline().split())) for _ in range(X)]

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]


def bfs(x, y, visit):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    count = 0
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < X and 0 <= next_y < Y:
                if visit[next_x][next_y] == 0:
                    visit[next_x][next_y] = 1
                    if cheeze[next_x][next_y] == 1:
                        cheeze[next_x][next_y] = 0
                        count += 1
                    else:
                        q.append([next_x, next_y])

    return count


N = 0
while True:
    visit = [[0]*Y for _ in range(X)]
    c = bfs(0, 0, visit)
    if c != 0:
        now_cheeze = c
        N += 1
    else:
        if N == 0:
            print(0)
            print(0)
        else:
            print(N)
            print(now_cheeze)
        break
