import sys
import heapq

INF = sys.maxsize

N, M, K = map(int, sys.stdin.readline().split())

graph = {}

for i in range(1, N+1):
    graph[i] = {}

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        if graph[u][v] > w:
            graph[u][v] = w
            graph[v][u] = w
    else:
        graph[u][v] = w
        graph[v][u] = w


def dijkstra(city, start, p):
    route = [[INF]*(p+1) for _ in range(N+1)]
    route[start][0] = 0

    heap = []
    heapq.heappush(heap, [route[start][0], start, 0])

    while heap:
        now_dist, now_pos, now_pack = heapq.heappop(heap)

        if route[now_pos][now_pack] < now_dist:
            continue

        for next_pos, next_dist in city[now_pos].items():
            if now_pack < p:
                if now_dist < route[next_pos][now_pack+1]:
                    route[next_pos][now_pack+1] = now_dist
                    heapq.heappush(heap, [now_dist, next_pos, now_pack+1])

            change_dist = now_dist + next_dist
            if change_dist < route[next_pos][now_pack]:
                route[next_pos][now_pack] = change_dist
                heapq.heappush(heap, [change_dist, next_pos, now_pack])

    return route


R = dijkstra(graph, 1, K)
print(min(R[N]))
