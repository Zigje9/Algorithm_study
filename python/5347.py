import sys

T = int(sys.stdin.readline())


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def solution():
    a, b = map(int, sys.stdin.readline().split())
    g = gcd(a, b)
    print(a*b//g)


while T > 0:
    solution()
    T -= 1
