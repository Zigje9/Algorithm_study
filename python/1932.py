import sys
N = int(sys.stdin.readline())

data = [[0 for i in range(N)] for j in range(N)]
dp = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    input_value = list(map(int, sys.stdin.readline().split()))
    for j in range(i+1):
        data[i][j] = input_value[j]

dp[0][0] = data[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + data[i][j]
        if j == i:
            dp[i][j] = dp[i-1][j-1] + data[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i][j]

print(max(dp[N-1]))
