import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

i = 0
j = N-1

if N == 1:
    print(0)
    sys.exit()

answer = 0
while i < j:
    if nums[i] + nums[j] > M:
        j -= 1

    elif nums[i] + nums[j] < M:
        i += 1

    else:
        answer += 1
        i += 1
        j -= 1

print(answer)
