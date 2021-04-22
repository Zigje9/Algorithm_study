import sys

N, K = map(int, sys.stdin.readline().split())

graph = [[0]*N for _ in range(N)]

for _ in range(K):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1][v-1] = -1
    graph[v-1][u-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and graph[i][j] == 0:
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    continue
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    continue


S = int(sys.stdin.readline())

for _ in range(S):
    u, v = map(int, sys.stdin.readline().split())
    print(graph[u-1][v-1])
