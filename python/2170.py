import sys

N = int(sys.stdin.readline())
num_list = []
for i in range(N):
    num_list.append(list(map(int, sys.stdin.readline().split())))


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[mid:])
#     right = merge_sort(arr[:mid])

#     sorted_list = []
#     left_idx = right_idx = 0
#     while left_idx < len(left) and right_idx < len(right):
#         if left[left_idx][0] <= right[right_idx][0]:
#             sorted_list.append(left[left_idx])
#             left_idx += 1
#         else:
#             sorted_list.append(right[right_idx])
#             right_idx += 1
#     sorted_list += left[left_idx:]
#     sorted_list += right[right_idx:]
#     return sorted_list


num_list.sort()

x = num_list[0][0]
y = num_list[0][1]
answer = 0
for i in range(1, len(num_list)):
    if num_list[i][0] <= y:
        if num_list[i][1] > y:
            y = num_list[i][1]
    else:
        answer += (y-x)
        x = num_list[i][0]
        y = num_list[i][1]
print(answer + y - x)
