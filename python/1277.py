import sys
import heapq

N, W = map(int, sys.stdin.readline().split())

M = float(sys.stdin.readline())

pos = [["X", "X"]]

for _ in range(N):
    pos.append(list(map(int, sys.stdin.readline().split())))

already = {}

graph = {}

for i in range(1, N+1):
    graph[i] = {}
    already[i] = {}

for _ in range(W):
    a, b = map(int, sys.stdin.readline().split())
    already[min(a, b)][max(a, b)] = True

for i in range(1, N):
    for j in range(i+1, N+1):
        if j in already[i]:
            graph[i][j] = 0
            graph[j][i] = 0
            continue
        x1, y1 = pos[i]
        x2, y2 = pos[j]
        dist = ((x2-x1)**2+(y2-y1)**2)**0.5
        if dist > M:
            continue
        graph[i][j] = dist
        graph[j][i] = dist

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


answer = dijkstra(graph, 1)[N]

if answer == INF:
    print(-1)
    sys.exit()

print(int(answer*1000))
