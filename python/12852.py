import sys

N = int(sys.stdin.readline())

DP = [0]*(N+1)

DP[1] = 0

for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)

    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)

print(DP[N])
answer = []
while N > 1:
    answer.append(N)
    c = []
    if N % 3 == 0:
        c.append([DP[N//3], N//3])

    if N % 2 == 0:
        c.append([DP[N//2], N//2])

    c.append([DP[N-1], N-1])

    c.sort()

    N = c[0][1]

answer.append(1)
print(" ".join(map(str, answer)))
