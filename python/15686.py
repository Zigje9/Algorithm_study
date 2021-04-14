import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

city = []

for _ in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

home = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
            continue

        if city[i][j] == 2:
            chicken.append([i, j])
            continue

answer = 2e9
if M == 1:
    for x, y in chicken:
        temp = 0
        for a, b in home:
            temp += abs(x-a) + abs(y-b)
        answer = min(answer, temp)
    print(answer)
    sys.exit()

for com in combinations(chicken, M):
    distance = 0
    for a, b in home:
        temp = 2e9
        for x, y in com:
            temp = min(temp, abs(x-a) + abs(y-b))
        distance += temp
    answer = min(answer, distance)

print(answer)
