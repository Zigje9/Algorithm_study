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

planet = []

for i in range(N+1):
    planet.append(i)

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

graphs = []

for i in range(N-1):
    for j in range(i+1, N):
        graphs.append([i+1, j+1, board[i][j]])

graph = sorted(graphs, key=lambda x: x[2])

count = 0
answer = 0
idx = 0
while count < N-1:
    A, B, dist = graph[idx]
    if get_parent(planet, A) == get_parent(planet, B):
        idx += 1
        continue
    union_parent(planet, A, B)
    answer += dist
    count += 1
    idx += 1

print(answer)
