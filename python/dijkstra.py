import heapq

INF = 2e9

graph = {
    1: {2: 2, 4: 1, 3: 5},
    2: {1: 2, 4: 2, 3: 3},
    3: {1: 5, 2: 3, 4: 3, 5: 1, 6: 5},
    4: {1: 1, 2: 2, 3: 3, 5: 1},
    5: {4: 1, 3: 1, 6: 2},
    6: {5: 2, 3: 5}
}

# 한 정점으로부터 모든 노드 까지의 최단거리


def dijkstra(city, start):
    route = {}
    for node in city:
        route[node] = INF

    route[start] = 0  # 시작 노드까지의 거리 0

    heap = []
    heapq.heappush(heap, [route[start], start])  # 우선 순위 큐에 [거리, 노드번호]로 집어넣음

    while heap:
        now_dist, now_pos = heapq.heappop(heap)

        if route[now_pos] < now_dist:  # 우선 순위 큐에서 나온 노드 까지의 거리를 갱신할 필요가 없으면 continue
            continue

        for next_pos, next_dist in city[now_pos].items():
            change_dist = now_dist + next_dist
            if change_dist < route[next_pos]:
                route[next_pos] = change_dist
                heapq.heappush(heap, [change_dist, next_pos])

    return route


r = dijkstra(graph, 1)
print(r)
# answer : {1: 0, 2: 2, 3: 3, 4: 1, 5: 2, 6: 4}
