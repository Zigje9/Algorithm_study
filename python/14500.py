import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

max_value = max(map(max, board))
move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

answer = 0

visit = [[False]*(M) for _ in range(N)]


def dfs(x, y, count, value):
    global answer
    if value + (4-count)*max_value <= answer:
        return

    if count == 4:
        answer = max(answer, value)
        return

    if count == 1:
        shape1, shape2, shape3, shape4 = 0, 0, 0, 0
        if 1 <= x < N and 1 <= y < M-1:
            shape1 = value + board[x-1][y] + board[x][y-1] + board[x][y+1]
        if 1 <= x < N-1 and 0 <= y < M-1:
            shape2 = value + board[x-1][y] + board[x+1][y] + board[x][y+1]
        if 0 <= x < N-1 and 1 <= y < M-1:
            shape3 = value + board[x][y-1] + board[x][y+1] + board[x+1][y]
        if 1 <= x < N-1 and 1 <= y < M:
            shape4 = value + board[x][y-1] + board[x-1][y] + board[x+1][y]
        answer = max(answer, shape1, shape2, shape3, shape4)

    for i in range(4):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if 0 <= next_x < N and 0 <= next_y < M and visit[next_x][next_y] == False:
            visit[next_x][next_y] = True
            dfs(next_x, next_y, count+1, value+board[next_x][next_y])
            visit[next_x][next_y] = False


for i in range(N):
    for j in range(M):
        visit[i][j] = True
        dfs(i, j, 1, board[i][j])
        visit[i][j] = False

print(answer)
