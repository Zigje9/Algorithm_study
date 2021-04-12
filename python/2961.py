import sys
from itertools import combinations

N = int(sys.stdin.readline())

cook = []

for _ in range(N):
    cook.append(list(map(int, sys.stdin.readline().split())))

answer = 2e9

for s, t in cook:
    answer = min(answer, abs(s-t))

for j in range(2, N+1):
    for com in combinations(cook, j):
        s = 1
        t = 0
        for k in range(j):
            s *= com[k][0]
            t += com[k][1]
        answer = min(answer, abs(s-t))

print(answer)
