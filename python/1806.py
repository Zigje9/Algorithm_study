import sys

N, S = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

i = 0
j = 1
temp = nums[0] + nums[1]
answer = 2e9
while i <= j < N-1:
    if temp < S:
        j += 1
        temp += nums[j]

    else:
        answer = min(answer, j-i+1)
        temp -= nums[i]
        i += 1

if temp >= S:
    while i <= j:
        answer = min(answer, j-i+1)
        temp -= nums[i]
        i += 1
        if temp < S:
            break

if answer == 2e9:
    print(0)
else:
    print(answer)
