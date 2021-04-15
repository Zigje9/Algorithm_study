import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline())

robot = []
count = [1] * 1000001
for i in range(1000001):
    robot.append(i)


def get_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a != b:
        count[b] += count[a]
        count[a] = 0
        robot[a] = b


answer = []

for _ in range(N):
    c = list(map(str, sys.stdin.readline().split()))
    if c[0] == "I":
        union_parent(robot, int(c[1]), int(c[2]))
    else:
        k = int(c[1])
        answer.append(count[get_parent(robot, k)])

for p in answer:
    print(p)
