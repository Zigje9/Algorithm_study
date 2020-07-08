N = int(input())
miro = []
for i in range(N):
    miro.append(list(map(int, input())))

finder = [[0 for i in range(N)] for j in range(N)]

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]

answer = []


def bfs(x, y):
    queue = []
    queue.insert(0, [x, y])
    finder[x][y] = 1
    temp = 1
    while len(queue) > 0 :
        now_x = queue[-1][0]
        now_y = queue[-1][1]
        queue.pop()
        for idx in range(4):
            next_x = now_x + move_x[idx]
            next_y = now_y + move_y[idx]
            if (next_x >= 0) and (next_y >= 0) and (next_x <= N-1) and (next_y <= N-1):
                if miro[next_x][next_y] == 1 and finder[next_x][next_y] == 0:
                    queue.insert(0, [next_x, next_y])
                    finder[next_x][next_y] = 1
                    temp += 1

    return temp


for i in range(N):
    for j in range(N):
        if finder[i][j] == 0 and miro[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))
answer = sorted(answer)
for i in answer:
    print(i)
