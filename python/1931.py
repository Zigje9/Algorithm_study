import sys
N = int(sys.stdin.readline())
num_list = []
for i in range(N):
    num_list.append(list(map(int, sys.stdin.readline().split())))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    temp_list = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx][1] <= right[right_idx][1]:
            if left[left_idx][1] == right[right_idx][1]:
                if left[left_idx][0] <= right[right_idx][0]:
                    temp_list.append(left[left_idx])
                    left_idx += 1
                else:
                    temp_list.append(right[right_idx])
                    right_idx += 1
            else:
                temp_list.append(left[left_idx])
                left_idx += 1
        else:
            temp_list.append(right[right_idx])
            right_idx += 1
    temp_list += left[left_idx:]
    temp_list += right[right_idx:]
    return temp_list


sorted_list = merge_sort(num_list)
answer = 0
now_max = 0
for conference in sorted_list:
    if conference[0] >= now_max:
        answer += 1
        now_max = conference[1]
print(answer)


# import sys
# N = int(sys.stdin.readline())
# conferlist = []
# for i in range(N):
#     conferlist.append(list(map(int, sys.stdin.readline().split())))
# conferlist = sorted(conferlist,reverse=True)
# point = conferlist[0][0]
# answer = 1
# for check in conferlist:
#     if check != conferlist[0]:
#         if check[1] <= point:
#             point = check[0]
#             answer += 1

# print(answer)
