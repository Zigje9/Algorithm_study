import sys


def get_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a != b:
        parent[b] = a


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    city = []

    for i in range(N):
        city.append(i)

    graph = []

    total = 0
    for _ in range(M):
        A, B, D = map(int, sys.stdin.readline().split())
        total += D
        graph.append([A, B, D])

    graph.sort(key=lambda x: x[2])

    idx = 0
    used = 0
    count = 0

    while count < N-1:
        A, B, dist = graph[idx]
        if get_parent(city, A) == get_parent(city, B):
            idx += 1
            continue

        union_parent(city, min(A, B), max(A, B))
        idx += 1
        count += 1
        used += dist

    print(total-used)
