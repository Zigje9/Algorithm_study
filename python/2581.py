import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

numbers = [1] * (N+1)
numbers[1] = 0
prime = []

for i in range(2, N+1):
    if numbers[i] == 1:
        if i >= M and i <= N:
            prime.append(i)
        for j in range(2*i, N+1, i):
            numbers[j] = 0

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
