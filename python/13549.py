import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

visit = [-1]*100001


def bfs():
    q = deque()
    visit[N] = 0
    q.append(N)
    while q:
        now = q.popleft()
        if now + 1 <= K and (visit[now+1] == -1 or visit[now+1] > visit[now] + 1):
            visit[now+1] = visit[now] + 1
            q.append(now+1)

        if now - 1 >= 0 and (visit[now-1] == -1 or visit[now-1] > visit[now] + 1):
            visit[now-1] = visit[now] + 1
            q.append(now-1)

        if now*2 <= 100000 and (visit[now*2] == -1 or visit[now*2] > visit[now]):
            visit[now*2] = visit[now]
            q.append(now*2)


bfs()
print(visit[K])
