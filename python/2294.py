import sys

n, k = map(int, sys.stdin.readline().split())

coin = []

for i in range(n):
    coin.append(int(sys.stdin.readline()))

set_coin = sorted(list(set(coin)))

dp = [1000000]*10001
dp[0] = 0

for i in range(1, k+1):
    for c in set_coin:
        if c > i:
            break
        dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == 1000000:
    print(-1)
else:
    print(dp[k])
