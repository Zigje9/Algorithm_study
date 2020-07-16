N = int(input())

DP = [0 for i in range(1000001)]

DP[2] = 1
DP[3] = 1
DP[4] = 2
DP[5] = 3

for i in range(6, 1000001):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)

print(DP[N])
