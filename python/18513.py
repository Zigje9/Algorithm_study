import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

refresh = list(map(int, sys.stdin.readline().split()))

visit = {}

answer = [0]


def bfs(count):
    q = deque()
    for s in refresh:
        visit[str(s)] = True
        q.append([s, 0, 0])  # 샘터 위치, 거리, 방향 0 -> 왼쪽
        q.append([s, 0, 1])
    while q:
        x, dist, direction = q.popleft()

        if direction == 0:  # 왼쪽으로만 이동
            if str(x-(dist+1)) not in visit:
                count -= 1
                q.append([x, dist+1, 0])
                answer[0] += (dist+1)
                visit[str(x-(dist+1))] = True
                if count == 0:
                    return

        if direction == 1:
            if str(x+(dist+1)) not in visit:
                count -= 1
                q.append([x, dist+1, 1])
                answer[0] += (dist+1)
                visit[str(x+(dist+1))] = True
                if count == 0:
                    return


bfs(K)

print(answer[0])
