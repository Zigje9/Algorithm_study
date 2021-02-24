import sys

H, W = map(int, sys.stdin.readline().split())

stone = list(map(int, sys.stdin.readline().split()))

rain = 0

for i in range(1, W-1):
    left_idx = i-1
    right_idx = i+1
    left_max_idx = right_max_idx = i

    while left_idx >= 0:
        if stone[left_idx] == H:
            left_max_idx = left_idx
            break
        if stone[left_idx] > stone[left_max_idx]:
            left_max_idx = left_idx
        left_idx -= 1

    while right_idx <= W-1:
        if stone[right_idx] == H:
            right_max_idx = right_idx
            break
        if stone[right_idx] > stone[right_max_idx]:
            right_max_idx = right_idx
        right_idx += 1
    rain += min(stone[left_max_idx], stone[right_max_idx]) - stone[i]

print(rain)
