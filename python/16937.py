import sys
from itertools import combinations

H, W = map(int, sys.stdin.readline().split())

N = int(sys.stdin.readline())

sticker = []

for _ in range(N):
    sticker.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for com in combinations(sticker, 2):
    A, B = com
    rotate_A = [A[1], A[0]]
    rotate_B = [B[1], B[0]]

    # 회전 안하고 가로로 붙임
    if A[1] + B[1] <= W and A[0] <= H and B[0] <= H:
        answer = max(answer, A[0]*A[1]+B[0]*B[1])
        continue
    if A[1] + rotate_B[1] <= W and A[0] <= H and rotate_B[0] <= H:
        answer = max(answer, A[0]*A[1]+rotate_B[0]*rotate_B[1])
        continue

    # 회전 하고 가로로 붙임
    if rotate_A[1] + B[1] <= W and rotate_A[0] <= H and B[0] <= H:
        answer = max(answer, rotate_A[0]*rotate_A[1]+B[0]*B[1])
        continue
    if rotate_A[1] + rotate_B[1] <= W and rotate_A[0] <= H and rotate_B[0] <= H:
        answer = max(answer, rotate_A[0]*rotate_A[1]+rotate_B[0]*rotate_B[1])
        continue

    # 회전 안하고 세로로 붙임
    if A[0] + B[0] <= H and A[1] <= W and B[1] <= W:
        answer = max(answer, A[0]*A[1]+B[0]*B[1])
        continue
    if A[0] + rotate_B[0] <= H and A[1] <= W and rotate_B[1] <= W:
        answer = max(answer, A[0]*A[1]+rotate_B[0]*rotate_B[1])
        continue

    # 회전 하고 세로로 붙임
    if rotate_A[0] + B[0] <= H and rotate_A[1] <= W and B[1] <= W:
        answer = max(answer, rotate_A[0]*rotate_A[1]+B[0]*B[1])
        continue
    if rotate_A[0] + rotate_B[0] <= H and rotate_A[1] <= W and rotate_B[1] <= W:
        answer = max(answer, rotate_A[0]*rotate_A[1]+rotate_B[0]*rotate_B[1])
        continue

print(answer)
