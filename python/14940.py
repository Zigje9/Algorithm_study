import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

move_x = [1, 0, -1, 0]
move_y = [0, -1, 0, 1]

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


def get_start():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                return [i, j]


visit = [[0]*M for _ in range(N)]

start_x, start_y = get_start()


def bfs():
    q = deque()
    q.append([start_x, start_y, 0])
    visit[start_x][start_y] = 2e9
    while q:
        now_x, now_y, dist = q.popleft()
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if visit[next_x][next_y] == 0 and board[next_x][next_y] == 1:
                    visit[next_x][next_y] = dist+1
                    q.append([next_x, next_y, dist+1])


bfs()

for i in range(N):
    for j in range(M):
        if visit[i][j] == 0 and board[i][j] == 1:
            visit[i][j] = -1

visit[start_x][start_y] = 0

for line in visit:
    print(" ".join(map(str, line)))
