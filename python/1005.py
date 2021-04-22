import sys
from collections import deque

T = int(sys.stdin.readline())


def solution():
    N, K = map(int, sys.stdin.readline().split())

    graph = {}
    for i in range(1, N+1):
        graph[i] = []

    degree = [[0]*2 for _ in range(N+1)]

    data = [0] + list(map(int, sys.stdin.readline().split()))

    for _ in range(K):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        degree[v][0] += 1

    find = int(sys.stdin.readline())

    def topo(craft):
        q = deque()

        for i in range(1, N+1):
            if degree[i][0] == 0:
                degree[i][1] = data[i]
                q.append(i)

        while q:
            now = q.popleft()

            for nx in craft[now]:
                degree[nx][0] -= 1
                degree[nx][1] = max(degree[nx][1], degree[now][1] + data[nx])
                if degree[nx][0] == 0:
                    q.append(nx)

    topo(graph)
    print(degree[find][1])


while T > 0:
    solution()
    T -= 1
