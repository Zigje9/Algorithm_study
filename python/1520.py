import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())

road = []
for _ in range(N):
    road.append(list(map(int, sys.stdin.readline().split())))

DP = [[-1] * M for _ in range(N)]

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1
    
    height = road[x][y]

    if DP[x][y] == -1:
        DP[x][y] = 0
        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if road[next_x][next_y] < height:
                    DP[x][y] += dfs(next_x, next_y)
    return DP[x][y]
print(dfs(0, 0))



