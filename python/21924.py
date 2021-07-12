import sys

N, M = map(int, sys.stdin.readline().split())

node = []
graph = []
for i in range(N+1):
    node.append(i)

for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

total = 0
for _, _, cost in graph:
    total += cost

graph.sort(key=lambda x: x[2])

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

count = 0
money = 0
idx = 0
while count < N-1:
    if idx > M-1:
        print(-1)
        sys.exit()

    A, B, cost = graph[idx]
    if get_parent(node, A) == get_parent(node, B):
        idx += 1
        continue

    union_parent(node, min(A, B), max(A, B))
    money += cost
    count += 1
    idx += 1

print(total-money)