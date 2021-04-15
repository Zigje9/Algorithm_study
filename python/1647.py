import sys

N, M = map(int, sys.stdin.readline().split())

city = []

for i in range(N+1):
    city.append(i)

graphs = []

for _ in range(M):
    graphs.append(list(map(int, sys.stdin.readline().split())))

graph = sorted(graphs, key=lambda x: x[2])


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


idx = 0
count = 0
answer = 0
max_value = 0
while count < N-1:
    A, B, dist = graph[idx]
    if get_parent(city, A) == get_parent(city, B):
        idx += 1
        continue

    union_parent(city, min(A, B), max(A, B))
    max_value = max(max_value, dist)
    answer += dist
    count += 1
    idx += 1

print(answer-max_value)
