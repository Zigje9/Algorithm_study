import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

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
        parent[a] = b
    else:
        parent[b] = a


def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    return False


for i in range(1, N+1):
    graph = list(map(int, sys.stdin.readline().split()))
    for j in range(len(graph)):
        if graph[j] == 1:
            union_parent(parent, i, j+1)

check_list = list(map(int, sys.stdin.readline().split()))
for i in range(len(check_list)-1):
    if find_parent(parent, check_list[i], check_list[i+1]):
        continue
    print("NO")
    sys.exit()
print("YES")
