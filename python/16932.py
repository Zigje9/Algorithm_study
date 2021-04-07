import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

visit = [[0]*M for _ in range(N)]
new_board = [[0]*M for _ in range(N)]


def bfs(x, y, t):
    c = 1
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < N and 0 <= next_y < M and visit[next_x][next_y] == 0:
                if board[next_x][next_y] != 0:
                    visit[next_x][next_y] = 1
                    q.append([next_x, next_y])
                    t.append([next_x, next_y])
                    c += 1

    return [t, c]


def check_in_temp(t, s):
    for x, y in t:
        if s[0] == x and s[1] == y:
            return False
    return True


idx = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and visit[i][j] == 0:
            idx += 1
            temp = []
            temp.append([i, j])
            T, count = bfs(i, j, temp)
            for x, y in T:
                new_board[x][y] = [count, idx]

answer = 0
for i in range(N):
    for j in range(M):
        if new_board[i][j] == 0:
            temp = []
            value = 1
            for k in range(4):
                next_x = i + move_x[k]
                next_y = j + move_y[k]
                if 0 <= next_x < N and 0 <= next_y < M and new_board[next_x][next_y] != 0:
                    if check_in_temp(temp, new_board[next_x][next_y]):
                        value += new_board[next_x][next_y][0]
                        temp.append(new_board[next_x][next_y])
            answer = max(value, answer)

print(answer)
