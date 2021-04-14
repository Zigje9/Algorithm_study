import sys

N, M = map(int, sys.stdin.readline().split())

parent = []

for i in range(N+1):
    parent.append(i)


def get_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    return False


for _ in range(M):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a, b):
            print("YES")
        else:
            print("NO")
