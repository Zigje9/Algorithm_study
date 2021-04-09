import sys

N, M = map(int, sys.stdin.readline().split())

num_list = [0] + list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (N+1)

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + num_list[i]

while M > 0:
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start-1])
    M -= 1
