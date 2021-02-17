import sys

N = int(sys.stdin.readline())

serial = []
for i in range(N):
    serial.append(sys.stdin.readline().rstrip())


def compare(a, b):
    if len(a) == len(b):
        sum_a = 0
        sum_b = 0
        for i in a:
            if i.isdigit():
                sum_a += int(i)
        for i in b:
            if i.isdigit():
                sum_b += int(i)
        if sum_a == sum_b:
            return a > b
        return sum_a > sum_b
    return len(a) > len(b)


def bubble_sort():
    for i in range(N):
        for j in range(N-i-1):
            if compare(serial[j], serial[j+1]):
                temp = serial[j]
                serial[j] = serial[j+1]
                serial[j+1] = temp


bubble_sort()
for i in range(N):
    print(serial[i])
