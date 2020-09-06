num_list = list(map(int, str(input())))


def bubble_sort(array):
    array_len = len(array)
    for i in range(array_len-1):
        for j in range(array_len-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


bubble_sort(num_list)
num_list.reverse()
num_list = list(map(str, num_list))
print("".join(num_list))