import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

answer = []

i = 0
j = 0

while i < N or j < M:
    if i == N:
        while j < M:
            answer.append(B[j])
            j += 1
        break

    if j == M:
        while i < N:
            answer.append(A[i])
            i += 1
        break

    if A[i] >= B[j]:
        answer.append(B[j])
        j += 1
    else:
        answer.append(A[i])
        i += 1

print(" ".join(map(str, answer)))
