import sys
from collections import deque

T = int(sys.stdin.readline())


def solution():
    N = int(sys.stdin.readline())
    graph = {}
    for i in range(1, N+1):
        graph[i] = {}

    degree = [0]*(N+1)

    before = list(map(int, sys.stdin.readline().split()))
    for i in range(len(before)-1):
        for j in range(i+1, len(before)):
            graph[before[i]][before[j]] = True
            degree[before[j]] += 1

    M = int(sys.stdin.readline())
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        if v in graph[u]:
            del graph[u][v]
            degree[u] += 1
            degree[v] -= 1
            graph[v][u] = True
        else:
            del graph[v][u]
            degree[v] += 1
            degree[u] -= 1
            graph[u][v] = True

    def topo(g):
        q = deque()
        answer = []
        for i in range(1, N+1):
            if degree[i] == 0:
                q.append(i)

        while q:
            if len(q) != 1:
                return -1
            now = q.popleft()
            answer.append(now)

            for nx in g[now].keys():
                degree[nx] -= 1
                if degree[nx] == 0:
                    q.append(nx)

        return answer

    a = topo(graph)
    if a == -1:
        print("?")
    else:
        if len(a) == N:
            print(" ".join(map(str, a)))
        else:
            print("IMPOSSIBLE")


while T > 0:
    solution()
    T -= 1
