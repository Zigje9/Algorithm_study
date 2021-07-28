import sys

N, M = map(int, sys.stdin.readline().split())

DP = [[0]*101 for _ in range(101)]

for i in range(101):
    for j in range(101):
        if j == 0:
            DP[i][j] = 1
            continue
        if i == j:
            DP[i][j] = 1
            break
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j]

print(DP[N][M])