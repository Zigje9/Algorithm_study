import sys

N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))


def bubble_sort(array):
    array_len = len(array)
    for i in range(array_len-1):
        for j in range(array_len-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def line_print(array):
    for i in array:
        print(i)


bubble_sort(num_list)
line_print(num_list)

