import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

visit = [[0]*M for _ in range(N)]

H, W, XS, YS, XF, YF = map(int, sys.stdin.readline().split())
XS -= 1
YS -= 1
XF -= 1
YF -= 1

answer = []


def bfs():
    q = deque()
    q.append([XS, YS, 0])
    visit[0][0] = 1
    while q:
        now_x, now_y, dist = q.popleft()
        if now_x == XF and now_y == YF:
            answer.append(dist)
            return

        if now_x+H < N:  # 아래로 이동
            if visit[now_x+1][now_y] == 0:  # 메인 좌표만 한칸 내린 것
                if sum(board[now_x+H][now_y:now_y+W]) == 0:  # 벽 없음
                    visit[now_x+1][now_y] = 1
                    q.append([now_x+1, now_y, dist+1])

        if now_y+W < M:  # 오른쪽으로 이동
            if visit[now_x][now_y+1] == 0:
                right_sum = 0
                for j in range(H):
                    right_sum += board[now_x+j][now_y+W]
                if right_sum == 0:
                    visit[now_x][now_y+1] = 1
                    q.append([now_x, now_y+1, dist+1])

        if 0 <= now_x-1:  # 위로 이동
            if visit[now_x-1][now_y] == 0:
                if sum(board[now_x-1][now_y:now_y+W]) == 0:
                    visit[now_x-1][now_y] = 1
                    q.append([now_x-1, now_y, dist+1])

        if 0 <= now_y-1:  # 왼쪽으로 이동
            if visit[now_x][now_y-1] == 0:
                left_sum = 0
                for j in range(H):
                    left_sum += board[now_x+j][now_y-1]
                if left_sum == 0:
                    visit[now_x][now_y-1] = 1
                    q.append([now_x, now_y-1, dist+1])


bfs()
if len(answer) == 0:
    print(-1)
else:
    print(answer[0])
