import sys

N = int(sys.stdin.readline())

for _ in range(N):
    print(sum(map(int, sys.stdin.readline().split())))
