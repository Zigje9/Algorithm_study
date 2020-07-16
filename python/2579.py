N = int(input())

stair = []
DP = []
stair.append(0)
DP.append(0)
for i in range(N):
    stair.append(int(input()))
    DP.append(0)


DP[1] = stair[1]

if N >= 2:
    DP[2] = stair[1] + stair[2]

if N >= 3:
    for i in range(3, N+1):
        DP[i] = max(DP[i-3] + stair[i] + stair[i-1], DP[i-2] + stair[i])

print(DP[N])

