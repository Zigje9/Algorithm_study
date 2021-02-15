import sys

N, M = map(int, sys.stdin.readline().split())

num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()


def solution():
    answer = 0
    left = num_list[0]
    right = num_list[-1]*M
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for el in num_list:
            if el > mid:
                break
            count += (mid // el)
        if count >= M:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)


solution()
