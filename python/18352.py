import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

city = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    city[A].append(B)

visit = [0] * (N+1)

answer = []


def bfs(start):
    q = deque()
    visit[start] = 1
    q.append([start, 0])
    while q:
        pos, dist = q.popleft()
        for next_pos in city[pos]:
            if visit[next_pos] == 0:
                if dist+1 == K:
                    answer.append(next_pos)
                if dist < K:
                    visit[next_pos] = 1
                    q.append([next_pos, dist+1])


bfs(X)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
