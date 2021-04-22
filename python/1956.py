import sys

INF = sys.maxsize

V, E = map(int, sys.stdin.readline().split())

road = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    road[u][v] = w

for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            road[i][j] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if road[i][j] > road[i][k] + road[k][j]:
                road[i][j] = road[i][k] + road[k][j]

answer = INF

for i in range(1, V):
    for j in range(i+1, V+1):
        if road[i][j] != INF and road[j][i] != INF:
            if answer > road[i][j] + road[j][i]:
                answer = road[i][j] + road[j][i]

if answer == INF:
    print(-1)
    sys.exit()

print(answer)
