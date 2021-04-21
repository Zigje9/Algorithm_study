import sys
import heapq
from collections import deque

INF = sys.maxsize

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

graph = {}

for i in range(1, N+1):
    graph[i] = {}

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        if graph[u][v] > w:
            graph[u][v] = w
    else:
        graph[u][v] = w

S, E = map(int, sys.stdin.readline().split())


def dijkstra(city, start):
    route = {}
    for node in city:
        route[node] = [INF, "before"]

    route[start][0] = 0
    route[start][1] = "start"

    heap = []
    heapq.heappush(heap, [route[start][0], start])

    while heap:
        now_dist, now_pos = heapq.heappop(heap)

        if route[now_pos][0] < now_dist:
            continue

        for next_pos, next_dist in city[now_pos].items():
            change_dist = next_dist + now_dist
            if change_dist < route[next_pos][0]:
                route[next_pos][0] = change_dist
                route[next_pos][1] = now_pos
                heapq.heappush(heap, [change_dist, next_pos])

    return route


R = dijkstra(graph, S)
print(R[E][0])
temp = deque()
temp.appendleft(E)
now = E
while True:
    if R[now][1] == 'start':
        break
    temp.appendleft(R[now][1])
    now = R[now][1]
print(len(temp))
print(" ".join(map(str, temp)))
