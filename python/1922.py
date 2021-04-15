import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graphs = []

for _ in range(M):
    graphs.append(list(map(int, sys.stdin.readline().split())))

network = []

for i in range(N+1):
    network.append(i)


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


graph = sorted(graphs, key=lambda x: x[2])

answer = 0
idx = 0
count = 0
while count < N-1:
    A, B, dist = graph[idx]
    if get_parent(network, A) == get_parent(network, B):
        idx += 1
        continue

    union_parent(network, min(A, B), max(A, B))
    answer += dist
    count += 1
    idx += 1

print(answer)
