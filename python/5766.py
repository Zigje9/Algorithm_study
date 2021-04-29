import sys

N, M = map(int, sys.stdin.readline().split())

num_list = []

for _ in range(N):
    num_list.append(list(map(int, sys.stdin.readline().split())))

K = int(sys.stdin.readline())

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    temp = 0
    for p in range(i-1, x):
        for q in range(j-1, y):
            temp += num_list[p][q]
    print(temp)
