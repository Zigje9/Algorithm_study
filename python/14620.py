import sys
from itertools import combinations

N = int(sys.stdin.readline())

board = []

move_x = [0, -1, 0, 1, 0]
move_y = [0, 0, 1, 0, -1]

answer = 2e9

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

position = []

for x in range(1, N-1):
    for y in range(1, N-1):
        position.append([x, y])

for com in combinations(position, 3):
    first, second, third = com
    if abs(first[0]-second[0])+abs(first[1]-second[1]) < 3:
        continue
    if abs(first[0]-third[0])+abs(first[1]-third[1]) < 3:
        continue
    if abs(second[0]-third[0])+abs(second[1]-third[1]) < 3:
        continue

    temp = 0
    for i in range(5):
        temp += board[first[0] + move_x[i]][first[1] + move_y[i]]
    for i in range(5):
        temp += board[second[0] + move_x[i]][second[1] + move_y[i]]
    for i in range(5):
        temp += board[third[0] + move_x[i]][third[1] + move_y[i]]

    answer = min(answer, temp)

print(answer)
