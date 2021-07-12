import sys

T = int(sys.stdin.readline())

def get_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

def solution():
    N = int(sys.stdin.readline())
    nodes = []
    for i in range(N+1):
        nodes.append(i)
    
    pos = []
    for _ in range(N):
        pos.append(list(map(int, sys.stdin.readline().split())))
    
    answer = N
    for i in range(N-1):
        for j in range(i+1, N):
            x1, y1, r1 = pos[i]
            x2, y2, r2 = pos[j]
            if ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) <= (r1+r2)*(r1+r2):
                if get_parent(nodes, i+1) != get_parent(nodes, j+1):
                    union_parent(nodes, i+1, j+1)
                    answer -= 1
    
    print(answer)


while T > 0:
    solution()
    T -= 1