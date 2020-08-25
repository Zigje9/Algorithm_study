import sys

F, S, G, U, D = map(int, sys.stdin.readline().split())
visit = [0]*(F+1)
q = []


def bfs(floor):
    q.append(floor)
    visit[floor] = 1
    while q:
        now_floor = q[0]
        q.pop(0)
        if now_floor == G:
            print(visit[now_floor]-1)
            return
        if now_floor + U <= F:
            if visit[now_floor + U] == 0:
                q.append(now_floor + U)
                visit[now_floor + U] = visit[now_floor] + 1
        if now_floor - D >= 1:
            if visit[now_floor - D] == 0:
                q.append(now_floor - D)
                visit[now_floor - D] = visit[now_floor] + 1
    print("use the stairs")


bfs(S)