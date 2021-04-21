import sys

INF = sys.maxsize

N, M = map(int, sys.stdin.readline().split())

graph = [[INF]*N for _ in range(N)]
board = [["-"]*N for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    if graph[u-1][v-1] > w:
        graph[u-1][v-1] = w
        graph[v-1][u-1] = w
        board[u-1][v-1] = v
        board[v-1][u-1] = u

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
                board[i][j] = board[i][k]

for b in board:
    print(" ".join(map(str, b)))
