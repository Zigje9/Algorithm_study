import sys

N = int(sys.stdin.readline())

DATA = [[False, False]]

for _ in range(N):
    DATA.append(list(map(int, sys.stdin.readline().split())))

DP = [0]*(N+2)

for i in range(N, 0, -1):
    day, money = DATA[i]
    work = 0
    if i + day - 1 <= N:
        work += money
        work += DP[i+day]

    DP[i] = max(work, DP[i+1])

print(DP[1])
