my_list = [3, 1, 11, 9, 5, 4, 2, 7, 21]


def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    mid = len(num_list) // 2
    left = merge_sort(num_list[:mid])
    right = merge_sort(num_list[mid:])

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


answer = merge_sort(my_list)
print(answer)
