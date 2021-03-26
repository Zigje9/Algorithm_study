import sys

money = int(sys.stdin.readline())

DP = [0]*100001

DP[2] = 1
DP[4] = 2
DP[5] = 1

for i in range(6, money+1):
    if DP[i-2] == 0 and DP[i-5] == 0:
        continue
    if DP[i-2] == 0 and DP[i-5] != 0:
        DP[i] = DP[i-5] + 1
        continue
    if DP[i-2] != 0 and DP[i-5] == 0:
        DP[i] = DP[i-2] + 1
        continue
    DP[i] = min(DP[i-2], DP[i-5]) + 1

if DP[money] == 0:
    print(-1)
else:
    print(DP[money])
