import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []

move_x = [1, 0, -1, 0]
move_y = [0, -1, 0, 1]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip())))

visit = [[[2e9]*M for _ in range(N)] for _ in range(2)]


def bfs():
    q = deque()
    q.append([0, 0, 0, 1])  # x, y, dist, drill
    visit[0][0][0] = 0
    while q:
        now_x, now_y, dist, drill = q.popleft()

        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if board[next_x][next_y] == 0 and visit[drill][next_x][next_y] == 2e9:
                    visit[drill][next_x][next_y] = dist+1
                    q.append([next_x, next_y, dist+1, drill])

        if drill == 1:
            for i in range(4):
                next_x = now_x + move_x[i]
                next_y = now_y + move_y[i]
                if 0 <= next_x < N and 0 <= next_y < M:
                    if board[next_x][next_y] == 1 and visit[drill-1][next_x][next_y] == 2e9:
                        visit[drill-1][next_x][next_y] = dist+1
                        q.append([next_x, next_y, dist+1, drill-1])


bfs()
answer = min(visit[0][N-1][M-1], visit[1][N-1][M-1])
if answer == 2e9:
    print(-1)
else:
    print(answer+1)
