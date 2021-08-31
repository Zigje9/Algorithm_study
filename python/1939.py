import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())

graph = {}

for i in range(1, N+1):
    graph[i] = {}

for _ in range(M):
    A, B, W = map(int, sys.stdin.readline().split())
    if B in graph[A]:
        if W > graph[A][B]:
            graph[A][B] = W
            graph[B][A] = W
    else:
        graph[A][B] = W
        graph[B][A] = W

start, end = map(int, sys.stdin.readline().split())

def bfs(m):
    v = [False]*(N+1)
    v[start] = True
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now == end:
            return True
        
        for next, weight in graph[now].items():
            if v[next] == False:
                if m <= weight:
                    q.append(next)
                    v[next] = True
    return False

left = 1
right = 1000000001

while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)




