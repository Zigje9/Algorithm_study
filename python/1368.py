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


N = int(sys.stdin.readline())

field = []
for i in range(N+1):
    field.append(i)

field_value = [0]
for _ in range(N):
    field_value.append(int(sys.stdin.readline()))

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

graphs = []

for i in range(1, N+1):
    graphs.append([0, i, field_value[i]])

for i in range(1, N):
    for j in range(i+1, N+1):
        graphs.append([i, j, board[i-1][j-1]])

graph = sorted(graphs, key=lambda x: x[2])

answer = 0
idx = 0
count = 0
while count < N:
    A, B, dist = graph[idx]
    if get_parent(field, A) == get_parent(field, B):
        idx += 1
        continue

    union_parent(field, A, B)
    answer += dist
    idx += 1
    count += 1

print(answer)
