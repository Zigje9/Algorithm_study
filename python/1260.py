N, M, start = map(int, input().split())

relation = [[0 for i in range(N+1)] for j in range(N+1)]

visit = [0 for k in range(N+1)]
visit2 = [0 for l in range(N+1)]

a_dfs = []
a_bfs = []

for i in range(M):
    x, y = map(int, input().split())
    relation[x][y] = 1
    relation[y][x] = 1


def dfs(st):
    if visit[st] == 1:
        return 0
    visit[st] = 1
    a_dfs.append(st)
    for i in range(1, N+1):
        if visit[i] == 0 and relation[st][i] == 1:
            dfs(i)


def bfs(st):
    queue = []
    queue.insert(0, st)
    visit2[st] = 1
    a_bfs.append(st)
    while len(queue) > 0:
        now = queue[-1]
        queue.pop()
        for i in range(1, N+1):
            if visit2[i] == 0 and relation[now][i] == 1:
                queue.insert(0, i)
                a_bfs.append(i)
                visit2[i] = 1


dfs(start)
bfs(start)

for i in a_dfs:
    print(i, end=' ')

print()

for j in a_bfs:
    print(j, end=' ')
