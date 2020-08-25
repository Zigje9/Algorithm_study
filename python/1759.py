import sys
from itertools import combinations
L, C = map(int, sys.stdin.readline().split())
Alpha = list(map(str, sys.stdin.readline().split()))

check = ["a", "e", "i", "o", "u"]

Alpha.sort()

for i in list(combinations(Alpha, L)):
    vv = 0
    cc = 0
    for vol in i:
        if vol in check:
            vv += 1
        else:
            cc += 1
    if vv >= 1 and cc >= 2:
        print(''.join(i))