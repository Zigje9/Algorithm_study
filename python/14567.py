import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = {}

for i in range(1, N+1):
    graph[i] = []

degree = [[0]*2 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    degree[v][0] += 1


def topo(subject):
    q = deque()

    for i in range(1, N+1):
        if degree[i][0] == 0:
            degree[i][1] = 1
            q.append(i)

    while q:
        now = q.popleft()

        for next_subject in graph[now]:
            degree[next_subject][0] -= 1
            if degree[next_subject][0] == 0:
                q.append(next_subject)
                degree[next_subject][1] = degree[now][1] + 1


topo(graph)
answer = []
for i in range(1, N+1):
    answer.append(degree[i][1])

print(" ".join(map(str, answer)))
