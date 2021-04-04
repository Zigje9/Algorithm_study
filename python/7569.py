import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

tomato = [[list(map(int, sys.stdin.readline().split()))
           for _ in range(N)] for _ in range(H)]

visit = [[[0]*M for _ in range(N)] for _ in range(H)]

move_x = [-1, 0, 1, 0, 0, 0]
move_y = [0, 1, 0, -1, 0, 0]
move_z = [0, 0, 0, 0, 1, -1]


def bfs():
    q = deque()
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if tomato[z][x][y] == 1:
                    q.append([z, x, y])
    while q:
        now_z, now_x, now_y = q.popleft()
        visit[now_z][now_x][now_y] = 1
        for i in range(6):
            next_z = now_z + move_z[i]
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_z < H and 0 <= next_x < N and 0 <= next_y < M:
                if visit[next_z][next_x][next_y] == 0 and tomato[next_z][next_x][next_y] == 0:
                    tomato[next_z][next_x][next_y] = tomato[now_z][now_x][now_y] + 1
                    visit[next_z][next_x][next_y] = 1
                    q.append([next_z, next_x, next_y])


bfs()
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[z][x][y] == 0:
                print(-1)
                sys.exit()

answer = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[z][x][y] > answer:
                answer = tomato[z][x][y]

print(answer-1)
