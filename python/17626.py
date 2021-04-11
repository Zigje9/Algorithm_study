# PyPy3 로 통과
import sys

N = int(sys.stdin.readline())

DP = [2e9]*(N+1)

DP[1] = 1

for i in range(2, N+1):
    if int(i**0.5)*int(i**0.5) == i:
        DP[i] = 1
        continue

    for j in range(1, int(i**0.5)+1):
        DP[i] = min(DP[i], DP[j*j] + DP[i-j*j])

print(DP[N])
