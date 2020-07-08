N, M = map(int, input().split())
miro = []
for i in range(N):
    miro.append(list(map(int, input())))

finder = [[0 for i in range(M)] for j in range(N)]

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]


def bfs(x, y):
    finder[x][y] = 1
    queue = []
    queue.insert(0, [x, y])
    while len(queue) > 0:
        now_x = queue[-1][0]
        now_y = queue[-1][1]
        queue.pop()
        for idx in range(4):
            next_x = now_x + move_x[idx]
            next_y = now_y + move_y[idx]
            if (next_x >= 0) and (next_y >= 0) and (next_x <= N-1) and (next_y <= M-1):
                if finder[next_x][next_y] == 0 and miro[next_x][next_y] == 1:
                    queue.insert(0, [next_x, next_y])
                    finder[next_x][next_y] = finder[now_x][now_y] + 1


bfs(0, 0)

print(finder[N-1][M-1])


