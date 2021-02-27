import sys

N = int(sys.stdin.readline())

DATA = [0] + list(map(int, sys.stdin.readline().split()))

DP = [0] * (N+1)

DP[1] = DATA[1]

DP[2] = max(DATA[1]*2, DATA[2])

for i in range(3, N+1):
    DP[i] = DATA[i]
    for j in range(1, i):
        if j > i:
            break
        DP[i] = max(DP[i], DP[j]+DP[i-j])

print(DP[N])
