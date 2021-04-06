import sys

N, M = map(int, sys.stdin.readline().split())

friend = [[] for _ in range(N)]

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    friend[X].append(Y)
    friend[Y].append(X)

answer = [False]


def dfs(now, visit, count):
    if count == 4:
        answer[0] = True
        return

    for f in friend[now]:
        if visit[f] == 0:
            visit[f] = 1
            dfs(f, visit, count+1)
            visit[f] = 0


for i in range(N):
    v = [0] * N
    v[i] = 1
    dfs(i, v, 0)
    if answer[0] == True:
        print(1)
        sys.exit()

print(0)
