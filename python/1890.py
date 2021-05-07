import sys

N = int(sys.stdin.readline())

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

DP = [[0]*N for _ in range(N)]

DP[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        dist = board[i][j]

        if dist + j <= N-1:
            DP[i][dist + j] += DP[i][j]
        if dist + i <= N-1:
            DP[dist + i][j] += DP[i][j]


print(DP[N-1][N-1])
