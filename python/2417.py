import sys

N = int(sys.stdin.readline())

left = 0
right = N
answer = 0
while left <= right:
    mid = (left + right) // 2
    if mid ** 2 < N:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
