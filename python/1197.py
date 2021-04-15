import sys

V, E = map(int, sys.stdin.readline().split())

node = []
graphs = []
for i in range(V+1):
    node.append(i)

for _ in range(E):
    graphs.append((list(map(int, sys.stdin.readline().split()))))

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


N = 0
distance = 0
idx = 0
while N < V-1:
    A, B, dist = graph[idx]
    if get_parent(node, A) == get_parent(node, B):
        idx += 1
        continue

    union_parent(node, A, B)
    distance += dist
    N += 1
    idx += 1

print(distance)
