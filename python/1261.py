import sys
from collections import deque

INF = sys.maxsize

M, N = map(int, sys.stdin.readline().split())

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

miro = []

for _ in range(N):
    miro.append(list(sys.stdin.readline().rstrip()))

visit = [[INF]*M for _ in range(N)]


def bfs(x, y):
    visit[x][y] = 0
    q = deque()
    q.append([x, y])
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < N and 0 <= next_y < M and visit[next_x][next_y] == INF:
                if miro[next_x][next_y] == "1":
                    visit[next_x][next_y] = visit[now_x][now_y] + 1
                    q.append([next_x, next_y])
                else:
                    visit[next_x][next_y] = visit[now_x][now_y]
                    q.appendleft([next_x, next_y])


bfs(0, 0)
print(visit[N-1][M-1])
