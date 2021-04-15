import sys

N, M = map(int, sys.stdin.readline().split())

node = []

for i in range(N+1):
    node.append(i)

pos = [[0, 0]]

for _ in range(N):
    pos.append(list(map(int, sys.stdin.readline().split())))

already = []
for _ in range(M):
    already.append(list(map(int, sys.stdin.readline().split())))


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


graphs = []

for i in range(1, N):
    for j in range(i+1, N+1):
        x1, y1 = pos[i]
        x2, y2 = pos[j]
        d = ((x2-x1)**2 + (y2-y1)**2)**0.5
        graphs.append([i, j, d])

graph = sorted(graphs, key=lambda x: x[2])

already_count = 0
for x, y in already:
    if get_parent(node, x) != get_parent(node, y):
        already_count += 1
        union_parent(node, min(x, y), max(x, y))

idx = 0
count = already_count
answer = 0

while count < N-1:
    A, B, dist = graph[idx]
    if get_parent(node, A) == get_parent(node, B):
        idx += 1
        continue

    union_parent(node, min(A, B), max(A, B))
    answer += dist
    idx += 1
    count += 1

print('%0.2f' % answer)
