import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())

node = []

for i in range(N):
    node.append(i)


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


graph = []
for _ in range(M):
    graph.append(sorted(list(map(int, sys.stdin.readline().split()))))

count = 0
idx = 0
while M > 0:
    A, B = graph[idx]
    count += 1
    if get_parent(node, A) != get_parent(node, B):
        union_parent(node, A, B)
    else:
        print(count)
        sys.exit()
    idx += 1
    M -= 1

print(0)
