import sys

N = int(sys.stdin.readline())

liquid = list(map(int, sys.stdin.readline().split()))

left = 0
right = N-1

answer = abs(liquid[0]+liquid[N-1])
answer_idx = [0, N-1]

while left < right:
    value = liquid[left] + liquid[right]
    if abs(value) <= answer:
        answer = abs(value)
        answer_idx = [left, right]

    if value >= 0:
        right -= 1
    else:
        left += 1


print(liquid[answer_idx[0]], liquid[answer_idx[1]])
