import sys

N, M = map(int, sys.stdin.readline().split())

DP = [[0]*M for _ in range(N)]

DATA = []

for _ in range(N):
    DATA.append(list(map(int, sys.stdin.readline().split())))

DP[0][0] = DATA[0][0]
for i in range(1, M):
    DP[0][i] = DP[0][i-1] + DATA[0][i]

for j in range(1, N):
    DP[j][0] = DP[j-1][0] + DATA[j][0]

for x in range(1, N):
    for y in range(1, M):
        DP[x][y] = max(max(DP[x-1][y-1], DP[x][y-1]), DP[x-1][y]) + DATA[x][y]

print(DP[N-1][M-1])
