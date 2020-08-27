import sys
t = int(input())
graph = [[] for _ in range(t+1)]
visit = [0]*(t+1)
answer = [0]*(t+1)
for i in range(t-1):
    m, n = map(int, sys.stdin.readline().split())
    graph[m].append(n)
    graph[n].append(m)


def bfs(root):
    q = [root]
    visit[root] = 1
    while q:
        pa = q[0]
        q.pop(0)
        for i in graph[pa]:
            if visit[i] == 0:
                q.append(i)
                answer[i] = pa
                visit[i] = 1


bfs(1)

for i in range(2, t+1):
    print(answer[i])



