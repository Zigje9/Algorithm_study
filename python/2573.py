# PyPy3로 통과
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

ice = []

for _ in range(N):
    ice.append(list(map(int, sys.stdin.readline().split())))

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]


def bfs(x, y, visit):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if visit[next_x][next_y] == 0 and ice[next_x][next_y] > 0:
                    visit[next_x][next_y] = 1
                    q.append([next_x, next_y])
                if ice[next_x][next_y] == 0:
                    if visit[next_x][next_y] == 0:
                        ice[now_x][now_y] -= 1
            if ice[now_x][now_y] < 0:
                ice[now_x][now_y] = 0


time = 0
while True:
    v = [[0]*M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] == 0 and ice[i][j] != 0:
                bfs(i, j, v)
                count += 1
                if count >= 2:
                    print(time)
                    sys.exit(0)
    if count == 0:
        print(0)
        sys.exit(0)
    time += 1
