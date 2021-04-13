import sys

N = int(sys.stdin.readline())

pos = []
for _ in range(N):
    pos.append(list(map(int, sys.stdin.readline().split())))


answer = 0

pos.append([pos[0][0], pos[0][1]])
A = 0
B = 0

for i in range(N):
    A += pos[i][0]*pos[i+1][1]
    B += pos[i+1][0]*pos[i][1]

print(round(abs(A-B)/2, 1))
