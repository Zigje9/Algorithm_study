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

star = []

for i in range(N+1):
    star.append(i)

star_pos = [[0, 0]]

for _ in range(N):
    star_pos.append(list(map(float, sys.stdin.readline().split())))

graphs = []

for i in range(1, N+1):
    for j in range(i+1, N+1):
        x1, y1 = star_pos[i]
        x2, y2 = star_pos[j]
        distance = round(((x2-x1)**2 + (y2-y1)**2)**0.5, 2)
        graphs.append([i, j, distance])

graph = sorted(graphs, key=lambda x: x[2])

count = 0
answer = 0
idx = 0
while count < N-1:
    A, B, dist = graph[idx]
    idx += 1
    if get_parent(star, A) == get_parent(star, B):
        continue

    answer += dist
    union_parent(star, A, B)
    count += 1

print(answer)
