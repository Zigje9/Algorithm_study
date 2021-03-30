import sys

T = int(sys.stdin.readline())


def solution():
    int(sys.stdin.readline())
    numlist = list(map(int, sys.stdin.readline().split()))
    print(min(numlist), max(numlist))


while T > 0:
    solution()
    T -= 1
