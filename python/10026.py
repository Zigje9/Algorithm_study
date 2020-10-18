import sys
N = int(sys.stdin.readline())

color = [[] for i in range(N)]
visit = [[0]*N for i in range(N)]

move_x = [1, 0, -1, 0]
move_y = [0, -1, 0, 1]

answer = 0
answer2 = 0

for i in range(N):
    colors = str(sys.stdin.readline()).rstrip()
    for j in colors:
        color[i].append(j)

def bfs(start_x, start_y):
    visit[start_x][start_y] = 1
    queue = []
    queue.append([start_x, start_y])
    while len(queue) != 0:
        now_x = queue[0][0]
        now_y = queue[0][1]
        now_color = color[now_x][now_y]
        queue.pop(0)
        for i in range(4):
            if now_x+move_x[i] >= 0 and now_x+move_x[i] < N and now_y+move_y[i] >= 0 and now_y+move_y[i] < N:
                next_x = now_x+move_x[i]
                next_y = now_y+move_y[i]
                if visit[next_x][next_y] == 0 and now_color == color[next_x][next_y]:
                    queue.append([next_x, next_y])
                    visit[next_x][next_y] = 1

for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            bfs(i, j)
            answer += 1

visit = [[0]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if color[i][j] == 'G':
            color[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            bfs(i, j)
            answer2 += 1

print(answer, answer2)