# PyPy3 로 통과

import sys

N = int(sys.stdin.readline())

INF = sys.maxsize

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

DP = [[INF]*N for _ in range(N)]

DP[0][0] = 0

for j in range(1, N):
    diff = board[0][j] - board[0][j-1]
    if diff >= 0:
        DP[0][j] = DP[0][j-1] + diff + 1
    else:
        DP[0][j] = DP[0][j-1]

for i in range(1, N):
    diff = board[i][0] - board[i-1][0]
    if diff >= 0:
        DP[i][0] = DP[i-1][0] + diff + 1
    else:
        DP[i][0] = DP[i-1][0]

for i in range(1, N):
    for j in range(1, N):
        if board[i][j]-board[i][j-1] >= 0:
            row = DP[i][j-1] + board[i][j]-board[i][j-1] + 1
        else:
            row = DP[i][j-1]

        if board[i][j]-board[i-1][j] >= 0:
            col = DP[i-1][j] + board[i][j]-board[i-1][j] + 1
        else:
            col = DP[i-1][j]

        DP[i][j] = min(row, col)

print(DP[N-1][N-1])
