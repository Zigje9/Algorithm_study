import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [[] for _ in range(N)]

for i in range(N):
    relation = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if len(relation) == 1:
        continue
    for re in relation[:-1]:
        graph[i].append(re-1)

M = int(sys.stdin.readline())

origin_rumor = list(map(int, sys.stdin.readline().split()))

state = [0] * N
answer = [-1] * N
spread_list = deque()

for rumor in origin_rumor:
    answer[rumor-1] = 0
    spread_list.append(rumor-1)

def bfs():
    while spread_list:
        spread_num = spread_list.popleft()
        for check_num in graph[spread_num]:
            state[check_num] += 1
            if answer[check_num] == -1:
                if state[check_num]*2 >= len(graph[check_num]):
                    spread_list.append(check_num)
                    answer[check_num] = answer[spread_num] + 1

bfs()

print(" ".join(map(str, answer)))