import sys
from collections import deque

K = int(sys.stdin.readline())

W, H = map(int, sys.stdin.readline().split())

horse = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]

jump_x = [-1, -2, -2, -1, 1, 2, 2, 1]
jump_y = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(x, y, jump, visit):
    q = deque()
    q.append([x, y, jump])
    visit[x][y][jump] = 0
    while q:
        now_x, now_y, now_j = q.popleft()

        if now_x == H-1 and now_y == W-1:
            return min(visit[now_x][now_y])

        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < H and 0 <= next_y < W:
                if visit[next_x][next_y][now_j] > visit[now_x][now_y][now_j] + 1 and horse[next_x][next_y] == 0:
                    visit[next_x][next_y][now_j] = visit[now_x][now_y][now_j] + 1
                    q.append([next_x, next_y, now_j])

        if now_j > 0:
            for j in range(8):
                next_x = now_x + jump_x[j]
                next_y = now_y + jump_y[j]
                if 0 <= next_x < H and 0 <= next_y < W:
                    if visit[next_x][next_y][now_j-1] > visit[now_x][now_y][now_j] + 1 and horse[next_x][next_y] == 0:
                        visit[next_x][next_y][now_j-1] = visit[now_x][now_y][now_j] + 1
                        q.append([next_x, next_y, now_j-1])
    return 2e9

visit = [[[2e9 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

answer = bfs(0, 0, K, visit)
if answer == 2e9:
    print(-1)
else:
    print(answer)
