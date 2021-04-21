import sys

INF = sys.maxsize

N = 4

graph = [[INF]*N for _ in range(N)]

input_arr = [[0, 5, INF, 8], [7, 0, 9, INF], [2, INF, 0, 4], [INF, INF, 3, 0]]

for i in range(N):
    for j in range(N):
        graph[i][j] = input_arr[i][j]


def floyd(city):
    for k in range(N):  # 거쳐가는 노드
        for i in range(N):  # 시작 노드
            for j in range(N):  # 도착 노드
                city[i][j] = min(city[i][k] + city[k][j], city[i][j])
    return city


print(floyd(graph))
