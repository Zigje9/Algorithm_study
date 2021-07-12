import sys

i = 1
max_value = 0
max_index = 0
while i<10:
    A = int(sys.stdin.readline())
    if max_value < A:
        max_value = A
        max_index = i
    i += 1

print(max_value)
print(max_index)