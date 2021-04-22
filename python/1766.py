import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = {}

for i in range(1, N+1):
    graph[i] = []

degree = [0]*(N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    degree[v] += 1


def topo(question):
    heap = []
    answer = []

    for i in range(1, N+1):
        if degree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        now = heapq.heappop(heap)
        answer.append(now)

        for nx in graph[now]:
            degree[nx] -= 1
            if degree[nx] == 0:
                heapq.heappush(heap, nx)

    return answer


a = topo(graph)

print(" ".join(map(str, a)))
