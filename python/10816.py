import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

nums = {}

for num in num_list:
    n = str(num)
    if n in nums:
        nums[n] += 1
    else:
        nums[n] = 1

M = int(sys.stdin.readline())

inputs = list(map(int, sys.stdin.readline().split()))

answer = []

for check in inputs:
    c = str(check)
    if c in nums:
        answer.append(nums[c])
    else:
        answer.append(0)

print(" ".join(map(str, answer)))
