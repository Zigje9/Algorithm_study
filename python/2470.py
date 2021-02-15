import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()


def solution():
    value = abs(num_list[0] + num_list[-1])
    left_value = num_list[0]
    right_value = num_list[-1]
    left = 0
    right = N-1
    while left < right:
        check_value = num_list[left] + num_list[right]
        if abs(check_value) < value:
            value = abs(check_value)
            left_value = num_list[left]
            right_value = num_list[right]
        if check_value < 0:
            left += 1
        else:
            right -= 1
    print(left_value, right_value)


solution()
