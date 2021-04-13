import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip())))

wall = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            wall.append([i, j])
            board[i][j] = -1


def bfs(x, y):
    p = []
    visit[x][y] = True
    p.append([x, y])
    count = 1
    q = deque()
    q.append([x, y])
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < N and 0 <= next_y < M and visit[next_x][next_y] == False:
                if board[next_x][next_y] == 0:
                    visit[next_x][next_y] = True
                    count += 1
                    q.append([next_x, next_y])
                    p.append([next_x, next_y])

    return count, p


idx = 0
visit = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            idx += 1
            c, pos = bfs(i, j)
            for x, y in pos:
                board[x][y] = [c, idx]

answer_board = [[0]*M for _ in range(N)]

for x, y in wall:
    value = 1
    s = []
    for i in range(4):
        find_x = x + move_x[i]
        find_y = y + move_y[i]
        if 0 <= find_x < N and 0 <= find_y < M:
            if board[find_x][find_y] != -1:
                if board[find_x][find_y] not in s:
                    s.append(board[find_x][find_y])

    for j in s:
        value += j[0]
    answer_board[x][y] = value % 10

for p in answer_board:
    print("".join(map(str, p)))
