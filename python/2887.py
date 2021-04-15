import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())

planet = []

node = []


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


for i in range(N):
    node.append(i)

for i in range(N):
    planet.append(list(map(int, sys.stdin.readline().split())) + [i])

graphs = []

for i in range(3):
    temp_planet = sorted(planet, key=lambda x: x[i])
    for j in range(N-1):
        graphs.append([temp_planet[j][3], temp_planet[j+1][3],
                       abs(temp_planet[j+1][i]-temp_planet[j][i])])

graph = sorted(graphs, key=lambda x: x[2])

answer = 0
idx = 0
count = 0
while count < N-1:
    A, B, dist = graph[idx]
    if get_parent(node, A) == get_parent(node, B):
        idx += 1
        continue

    union_parent(node, A, B)
    answer += dist
    count += 1
    idx += 1
print(answer)
