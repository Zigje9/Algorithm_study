import sys

power = {}
nums = []

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    keyword, value = map(str, sys.stdin.readline().split())
    power_num = int(value)
    if power_num not in power:
        power[power_num] = keyword

for _ in range(M):
    num = int(sys.stdin.readline())
    nums.append(num)

level = sorted(power.keys())
l = len(level)
def binarySearch(f):
    left = 0
    right = l-1
    while left <= right:
        mid = (left + right) // 2
        if f <= level[mid]:
            if level[mid-1] < f:
                break
            right = mid-1
        else:
            left = mid+1
    print(power[level[mid]])

for k in nums:
    binarySearch(k)
