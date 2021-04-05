# PyPy3 로 제출
import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())

country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]


def alliance(x, y, value, position):
    q = deque()
    q.append([x, y])
    count = 1
    total = country[x][y]
    visit[x][y] = value
    position.append([x, y, value])
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if visit[next_x][next_y] == 0 and L <= abs(country[now_x][now_y]-country[next_x][next_y]) <= R:
                    q.append([next_x, next_y])
                    visit[next_x][next_y] = value
                    count += 1
                    total += country[next_x][next_y]
                    position.append([next_x, next_y, value])

    return [count, total]


answer = 0


def isright(x, y):
    for i in range(4):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if visit[next_x][next_y] == 0 and L <= abs(country[x][y]-country[next_x][next_y]) <= R:
                return True
    return False


while True:
    visit = [[0]*N for _ in range(N)]
    VCT = []
    value = 1
    position = []
    for x in range(N):
        for y in range(N):
            if visit[x][y] == 0 and isright(x, y):
                c, total = alliance(x, y, value, position)
                if c > 1:
                    VCT.append([value, c, total])
                    value += 1
    for x, y, v in position:
        k = VCT[v-1]
        country[x][y] = k[2]//k[1]

    if len(position) == 0:
        break
    else:
        answer += 1

print(answer)
