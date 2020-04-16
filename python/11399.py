import sys
num = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0
for i in range(num):
    sum += (num-i)*num_list[i]
print(sum)