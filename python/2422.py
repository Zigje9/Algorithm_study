import sys

N, M = map(int, sys.stdin.readline().split())

check = [[True]*(N+1) for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    check[A][B] = False
    check[B][A] = False

answer = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if check[i][j]:
            for k in range(j+1, N+1):
                if check[i][k] and check[j][k]:
                    answer += 1

print(answer)
