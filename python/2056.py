import sys
from collections import deque

N = int(sys.stdin.readline())

graph = {}

for i in range(1, N+1):
    graph[i] = []

degree = [[0]*2 for _ in range(N+1)]
data = [0]*(N+1)

for i in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().split()))
    data[i] = temp[0]
    for j in temp[2:]:
        graph[j].append(i)
        degree[i][0] += 1


def topo(work):
    q = deque()

    for i in range(1, N+1):
        if degree[i][0] == 0:
            degree[i][1] = data[i]
            q.append(i)

    while q:
        now = q.popleft()

        for nx in work[now]:
            degree[nx][1] = max(degree[nx][1], data[nx] + degree[now][1])
            degree[nx][0] -= 1
            if degree[nx][0] == 0:
                q.append(nx)


topo(graph)

print(max(degree, key=lambda x: x[1])[1])
