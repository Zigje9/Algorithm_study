import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

preference = []

for _ in range(N):
    preference.append(list(map(int, sys.stdin.readline().split())))

answer = 0

chicken = []
for i in range(M):
    chicken.append(i)

for com in combinations(chicken, 3):
    A, B, C = com
    temp = 0
    for person in preference:
        temp += max(person[A], person[B], person[C])

    answer = max(answer, temp)

print(answer)
