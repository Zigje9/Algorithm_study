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


N, P = map(int, sys.stdin.readline().split())

country = []

for i in range(N+1):
    country.append(i)

country_cost = [2e9] * (N+1)

for i in range(1, N+1):
    country_cost[i] = int(sys.stdin.readline())

graphs = []

for _ in range(P):
    graphs.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(graphs)):
    A, B, dist = graphs[i]
    graphs[i][2] = country_cost[A]+country_cost[B]+2*dist

graph = sorted(graphs, key=lambda x: x[2])

idx = 0
answer = 0
count = 0
while count < N-1:
    A, B, dist = graph[idx]
    if get_parent(country, A) == get_parent(country, B):
        idx += 1
        continue

    union_parent(country, min(A, B), max(A, B))
    answer += dist
    count += 1
    idx += 1

print(answer + min(country_cost))
