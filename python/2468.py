import sys
from collections import deque

N = int(sys.stdin.readline())

board = []
max_rain = 0
answer = []

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]

def bfs(v, x, y, rain):
    q = deque()
    q.append([x, y])
    while q:
        now_pos = q.popleft()
        now_x = now_pos[0]
        now_y = now_pos[1]
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x <= N-1 and 0 <= next_y <= N-1:
                if v[next_x][next_y] == 0 and board[next_x][next_y] > rain:
                    q.append([next_x, next_y])
                    v[next_x][next_y] = 1

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    max_temp = max(temp)
    if max_temp > max_rain:
        max_rain = max_temp
    board.append(temp)

for rain in range(0, max_rain+1):
    visit = [[0]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and board[i][j] > rain:
                visit[i][j] = 1
                bfs(visit, i, j, rain)
                count += 1
    
    answer.append(count)

print(max(answer))


