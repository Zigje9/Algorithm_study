import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[0]*N for _ in range(N)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = -1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and i != j:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    continue
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    continue

for i in range(N):
    print(graph[i].count(0)-1)
