import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = {}
for i in range(1, N+1):
    graph[i] = []

degree = [0]*(N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    degree[v] += 1


def topo(students):
    q = deque()

    answer = []

    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        answer.append(now)

        for next_person in students[now]:
            degree[next_person] -= 1
            if degree[next_person] == 0:
                q.append(next_person)

    return answer


a = topo(graph)
print(" ".join(map(str, a)))
