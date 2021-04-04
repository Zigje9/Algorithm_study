# PyPy3 로 통과

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)


def bfs(start):
    count = 0
    visit = [0] * (N+1)
    visit[start] = 1
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        count += 1
        for next_node in graph[now]:
            if visit[next_node] == 0:
                q.append(next_node)
                visit[next_node] = 1

    return count


answer = []
max_value = 1
for i in range(1, N+1):
    virus = bfs(i)
    max_value = max(virus, max_value)
    answer.append([i, virus])

result = []
for el in list(filter(lambda x: x[1] >= max_value, answer)):
    result.append(el[0])

print(" ".join(map(str, result)))
