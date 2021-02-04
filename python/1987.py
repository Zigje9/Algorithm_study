''' DFS, dictionary 이용, pypy, python 시간초과
import sys
N, M = map(int, sys.stdin.readline().split())
road = []
for i in range(N):
    road.append(list(map(str, sys.stdin.readline().rstrip())))
answer = 1

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def dfs(x, y, distance, visit, check):
    global answer
    for i in range(4):
        next_x = x + move_x[i]
        next_y = y + move_y[i]

        if next_x >= 0 and next_y >= 0 and next_x < N and next_y < M:
            if visit[next_x][next_y] == 0 and check[road[next_x][next_y]] == 0:
                visit[next_x][next_y] = 1
                check[road[next_x][next_y]] = 1
                dfs(next_x, next_y, distance+1, visit, check)
                if answer <= distance:
                    answer = distance + 1
                visit[next_x][next_y] = 0
                check[road[next_x][next_y]] = 0


def solution():
    visit = [[0 for _ in range(M)] for j in range(N)]
    check = {}
    for e in alpha:
        check[e] = 0

    check[road[0][0]] = 1
    visit[0][0] = 1
    distance = 1

    dfs(0, 0, distance, visit, check)

    print(answer)


solution()
'''

''' DFS, ASCII 코드로 Array 이용, pypy 통과 python 시간초과
import sys
N, M = map(int, sys.stdin.readline().split())
road = []
for i in range(N):
    road.append(list(map(str, sys.stdin.readline().rstrip())))
answer = 1

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]


def dfs(x, y, distance, visit, alpha):
    global answer
    for i in range(4):
        next_x = x + move_x[i]
        next_y = y + move_y[i]

        if next_x >= 0 and next_y >= 0 and next_x < N and next_y < M:
            if visit[next_x][next_y] == 0 and alpha[ord(road[next_x][next_y])-65] == 0:
                visit[next_x][next_y] = 1
                alpha[ord(road[next_x][next_y])-65] = 1
                dfs(next_x, next_y, distance+1, visit, alpha)
                if answer <= distance:
                    answer = distance + 1
                visit[next_x][next_y] = 0
                alpha[ord(road[next_x][next_y])-65] = 0


def solution():
    visit = [[0 for _ in range(M)] for j in range(N)]
    alpha = [0]*26
    alpha[ord(road[0][0])-65] = 1

    visit[0][0] = 1
    distance = 1

    dfs(0, 0, distance, visit, alpha)

    print(answer)


solution()
'''

''' BFS https://devjin-blog.com/boj-1987-alphabet/ 참고
import sys
N, M = map(int, sys.stdin.readline().split())
road = []
for i in range(N):
    road.append(list(map(str, sys.stdin.readline().rstrip())))

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]


def bfs():
    answer = 1
    q = set([(0, 0, road[0][0])])
    while len(q) != 0:
        x, y, path = q.pop()
        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if next_x >= 0 and next_y >= 0 and next_x < N and next_y < M:
                if road[next_x][next_y] not in path:
                    q.add((next_x, next_y, path+road[next_x][next_y]))
                    answer = max(answer, len(path)+1)
    return answer


def solution():
    print(bfs())


solution()
'''
