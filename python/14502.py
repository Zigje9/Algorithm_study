import sys
import itertools
import copy

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]

Y, X = map(int, sys.stdin.readline().split())
def dfs(visit, city, start_x, start_y):
  if visit[start_x][start_y] == 0:
    visit[start_x][start_y] = 1
    if city[start_x][start_y] == 0:
      city[start_x][start_y] = 2
    for i in range(4):
      next_x = start_x + move_x[i]
      next_y = start_y + move_y[i]
      if next_x >= 0 and next_x < Y and next_y >= 0 and next_y < X:
        if visit[next_x][next_y] == 0 and city[next_x][next_y] != 1:
          dfs(visit, city, next_x, next_y)
  return city

ct = []

for i in range(Y):
  ct.append(list(map(int, sys.stdin.readline().split())))

empty = []

for i in range(Y):
  for j in range(X):
    if ct[i][j] == 0:
      empty.append([i,j])

wall_list = list(itertools.combinations(empty, 3))

max_answer = 0

for wall in wall_list:
  now_city = copy.deepcopy(ct)
  now_city[wall[0][0]][wall[0][1]] = 1
  now_city[wall[1][0]][wall[1][1]] = 1
  now_city[wall[2][0]][wall[2][1]] = 1
  answer = 0
  vt = [[0 for i in range(X)] for j in range(Y)]
  for i in range(Y):
    for j in range(X):
      if now_city[i][j] == 2:
        now_city = dfs(vt, now_city, i, j)
  for i in range(Y):
    for j in range(X):
      if now_city[i][j] == 0:
        answer += 1
  if max_answer < answer:
    max_answer = answer

print(max_answer)
