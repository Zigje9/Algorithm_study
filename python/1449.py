import sys

N, L = map(int, sys.stdin.readline().split())
tape = list(map(int, sys.stdin.readline().split()))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1
    sorted_list += left[left_idx:]
    sorted_list += right[right_idx:]
    return sorted_list


def solution():
    sorted_tape = merge_sort(tape)
    max_tape = sorted_tape[0]-0.5 + L
    answer = 1
    for hole in sorted_tape[1:]:
        if hole > max_tape:
            max_tape = hole-0.5 + L
            answer += 1
    print(answer)


solution()
