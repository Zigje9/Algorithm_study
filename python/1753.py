import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

s = int(sys.stdin.readline())

graph = {}

for i in range(1, V+1):
    graph[i] = {}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        if graph[u][v] > w:
            graph[u][v] = w
    else:
        graph[u][v] = w

INF = 2e9


def dijkstra(city, start):
    route = {}
    for node in city:
        route[node] = INF

    route[start] = 0

    heap = []
    heapq.heappush(heap, [route[start], start])

    while heap:
        now_dist, now_pos = heapq.heappop(heap)

        if route[now_pos] < now_dist:
            continue

        for next_pos, next_dist in city[now_pos].items():
            change_dist = now_dist + next_dist
            if change_dist < route[next_pos]:
                route[next_pos] = change_dist
                heapq.heappush(heap, [change_dist, next_pos])

    return route


answer = dijkstra(graph, s)
for i in range(1, V+1):
    if answer[i] == INF:
        print("INF")
        continue
    print(answer[i])
