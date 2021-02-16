import sys

N, C = map(int, sys.stdin.readline().split())

home = []
for i in range(N):
    home.append(int(sys.stdin.readline()))

home.sort()


def solution():
    left = 1
    right = home[-1] - home[0]
    answer = 1
    while left <= right:
        mid = (left + right) // 2
        first_home = home[0]
        count = 1
        for i in range(1, N):
            if mid <= home[i] - first_home:
                count += 1
                first_home = home[i]
        if C > count:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    print(answer)


solution()

# 거리의 최소를 left, 최대를 right 로 설정하고 이분탐색
