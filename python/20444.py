import sys

N, K = map(int, sys.stdin.readline().split())


def binarySearch(left, right):
    while left <= right:
        mid = (left + right) // 2
        value = (mid+1) * ((N-mid)+1)
        if value > K:
            right = mid - 1
        elif value < K:
            left = mid + 1
        else:
            print('YES')
            return
    print('NO')
    return

binarySearch(0, N//2)