import sys
import heapq

INF = sys.maxsize

N, M, R = map(int, sys.stdin.readline().split())

score = [0] + list(map(int, sys.stdin.readline().split()))

graph = {}

for i in range(1, N+1):
    graph[i] = {}

for _ in range(R):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        if graph[u][v] > w:
            graph[u][v] = w
            graph[v][u] = w
    else:
        graph[u][v] = w
        graph[v][u] = w


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


answer = 0

for i in range(1, N+1):
    new_route = dijkstra(graph, i)
    item = score[i]
    for j in range(1, N+1):
        if i == j:
            continue
        if new_route[j] <= M:
            item += score[j]
    answer = max(answer, item)

print(answer)
