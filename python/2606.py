import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

relation = []
visit = [0 for i in range(N+1)]

for i in range(N+1):
    relation.append([])

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    relation[A].append(B)
    relation[B].append(A)


def bfs(start):
    queue = []
    queue.append(start)
    visit[start] = 1
    while len(queue) != 0:
        now = queue[0]
        queue.pop(0)
        for ele in relation[now]:
            if visit[ele] == 0:
                queue.append(ele)
                visit[ele] = 1

bfs(1)
print(sum(visit)-1)