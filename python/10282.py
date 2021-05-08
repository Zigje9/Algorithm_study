import sys
import heapq

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


T = int(sys.stdin.readline())


def solution():
    n, d, start = map(int, sys.stdin.readline().split())
    graph = {}
    for i in range(1, n+1):
        graph[i] = {}

    for _ in range(d):
        B, A, dist = map(int, sys.stdin.readline().split())
        graph[A][B] = dist

    count = 0
    answer = 0
    for key, value in dijkstra(graph, start).items():
        if value != INF:
            count += 1
            answer = max(answer, value)

    print(count, answer)


while T > 0:
    solution()
    T -= 1
