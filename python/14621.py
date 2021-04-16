import sys

N, M = map(int, sys.stdin.readline().split())

node = []

for i in range(N+1):
    node.append(i)

univ = ["S"] + list(sys.stdin.readline().rstrip().split(" "))

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
answer = 0
count = 0

while count < N-1:
    if idx == len(graph):
        print(-1)
        sys.exit()
    A, B, dist = graph[idx]
    if univ[A] == univ[B]:
        idx += 1
        continue

    if get_parent(node, A) == get_parent(node, B):
        idx += 1
        continue

    union_parent(node, min(A, B), max(A, B))
    idx += 1
    answer += dist
    count += 1

print(answer)
