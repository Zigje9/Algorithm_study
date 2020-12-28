import sys

T = int(sys.stdin.readline())

move_x = [1, 0, -1, 0]
move_y = [0, 1, 0, -1]

def bfs(ground, visit, start_x, start_y, answer):
  visit[start_x][start_y] = 1
  q = []
  q.append([start_x, start_y])
  answer[0] += 1
  while(len(q) != 0):
    now_x = q[0][0]
    now_y = q[0][1]
    q.pop(0)
    for i in range(4):
      next_x = now_x + move_x[i]
      next_y = now_y + move_y[i]
      if next_x >= 0 and next_x < M and next_y >= 0 and next_y < N:
        if visit[next_x][next_y] == 0 and ground[next_x][next_y]==1:
          q.append([next_x, next_y])
          visit[next_x][next_y] = 1

while T > 0:
  M, N, K = map(int, sys.stdin.readline().split())
  ground = [[0 for i in range(N)] for j in range(M)]
  visit = [[0 for i in range(N)] for j in range(M)]
  answer = [0]
  while K > 0:
    a, b = map(int, sys.stdin.readline().split())
    ground[a][b] = 1
    K -= 1
  for i in range(M):
    for j in range(N):
      if(visit[i][j]==0 and ground[i][j]==1):
        bfs(ground, visit, i, j, answer)
  print(answer[0])
  T -= 1


