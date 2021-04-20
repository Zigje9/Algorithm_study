import sys
import heapq

N, E = map(int, sys.stdin.readline().split())

graph = {}
for i in range(1, N+1):
    graph[i] = {}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        if graph[u][v] > w:
            graph[u][v] = w
            graph[v][u] = w
            continue
    else:
        graph[u][v] = w
        graph[v][u] = w

A, B = map(int, sys.stdin.readline().split())

INF = sys.maxsize


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


start_1 = dijkstra(graph, 1)
goto_A = start_1[A]
goto_B = start_1[B]
start_A = dijkstra(graph, A)
A_B = start_A[B]
A_N = start_A[N]
B_N = dijkstra(graph, B)[N]

route_A = goto_A + A_B + B_N
route_B = goto_B + A_B + A_N
if route_A >= INF and route_B >= INF:
    print(-1)
    sys.exit()

print(min(route_A, route_B))
