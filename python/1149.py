import sys

N = int(sys.stdin.readline())

DATA = []

for _ in range(N):
    DATA.append(list(map(int, sys.stdin.readline().split())))

DP = [[0 for _ in range(3)] for _ in range(N)]

DP[0][0] = DATA[0][0]
DP[0][1] = DATA[0][1]
DP[0][2] = DATA[0][2]

for i in range(1, N):
    DP[i][0] = DATA[i][0] + min(DP[i-1][1], DP[i-1][2])
    DP[i][1] = DATA[i][1] + min(DP[i-1][0], DP[i-1][2])
    DP[i][2] = DATA[i][2] + min(DP[i-1][0], DP[i-1][1])

print(min(DP[N-1]))
