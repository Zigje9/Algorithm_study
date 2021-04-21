import sys

INF = sys.maxsize

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

graph = [[INF]*N for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    if graph[u-1][v-1] > w:
        graph[u-1][v-1] = w


def floyd(city):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                city[i][j] = min(city[i][j], city[i][k]+city[k][j])

    return city


answer = floyd(graph)

for i in range(N):
    for j in range(N):
        if answer[i][j] == INF:
            answer[i][j] = 0

for a in answer:
    print(" ".join(map(str, a)))
