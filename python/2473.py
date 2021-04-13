import sys

N = int(sys.stdin.readline())

liquid = sorted(list(map(int, sys.stdin.readline().split())))

answer = abs(liquid[0] + liquid[1] + liquid[N-1])
answer_idx = [0, 1, N-1]
for choice in range(N-2):
    choice_value = liquid[choice]
    left = choice+1
    right = N-1
    while left < right:
        value = choice_value + liquid[left] + liquid[right]
        if abs(value) <= answer:
            answer = abs(value)
            answer_idx = [choice, left, right]

        if value <= 0:
            left += 1
        else:
            right -= 1

print(liquid[answer_idx[0]], liquid[answer_idx[1]], liquid[answer_idx[2]])
