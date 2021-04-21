# PyPy3 로 통과
# Python3 코드로 시간초과, 정답 코드중 변수명만 다른, 같은 코드로 했는데도 시간초과 뭔가잘못된듯...

import sys

N, M = map(int, sys.stdin.readline().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def floyd(city):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                city[i][j] = min(city[i][j], city[i][k]+city[k][j])

    return city


party = floyd(graph)

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    if party[u-1][v-1] <= w:
        print("Enjoy other party")
    else:
        print("Stay here")
