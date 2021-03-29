# PyPy3로 통과 python3 시간초과
import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


g = gcd(numbers[0], numbers[1])
if len(numbers) == 3:
    g = gcd(g, numbers[2])

for i in range(1, g+1):
    if g % i == 0:
        print(i)
