import sys

N, K = map(int, sys.stdin.readline().split())

bag = []

for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    bag.append([W, V])

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < bag[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i-1][0]] + bag[i-1][1])

print(dp[N][K])
