import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())

knight = []

visit = [[0]*M for _ in range(N)]

move_x = [0, -1, 0, 1]
move_y = [-1, 0, 1, 0]

for _ in range(N):
    knight.append(list(map(int, sys.stdin.readline().split())))


def bfs():
    sword = 0
    q = deque()
    q.append([0, 0, 0])
    visit[0][0] = 1
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            next_dist = dist + 1
            if 0 <= next_x < N and 0 <= next_y < M:
                if visit[next_x][next_y] == 0 and knight[next_x][next_y] != 1:
                    if knight[next_x][next_y] == 2:
                        sword = next_dist + abs(next_x-N+1) + abs(next_y-M+1)

                    if next_x == N-1 and next_y == M-1:
                        visit[N-1][M-1] = next_dist
                        return sword
                    visit[next_x][next_y] = 1
                    q.append([next_x, next_y, next_dist])
    return sword


s = bfs()
if s == 0:
    if visit[N-1][M-1] == 0 or visit[N-1][M-1] > T:
        print("Fail")
    else:
        print(visit[N-1][M-1])
else:
    if visit[N-1][M-1] == 0:
        if s > T:
            print("Fail")
        else:
            print(s)
    else:
        if min(s, visit[N-1][M-1]) > T:
            print("Fail")
        else:
            print(min(s, visit[N-1][M-1]))
