import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()


def binary(left, right, value):
    while left <= right:
        mid = (left+right) // 2
        if num_list[mid] == value:
            return 1
        elif num_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return 0


def solution():
    for val in check_list:
        print(binary(0, N-1, val))


solution()
