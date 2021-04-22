import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

degree = [0]*(N+1)

graph = {}

for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    people = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(len(people)-1):
        graph[people[i]].append(people[i+1])
        degree[people[i+1]] += 1


def topo(g):
    answer = []
    q = deque()

    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        answer.append(now)

        for next_person in graph[now]:
            degree[next_person] -= 1
            if degree[next_person] == 0:
                q.append(next_person)

    return answer


a = topo(graph)

if len(a) != N:
    print(0)
    sys.exit()

for p in a:
    print(p)
