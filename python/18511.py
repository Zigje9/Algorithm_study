import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())

K = list(map(int, sys.stdin.readline().split()))
K.sort()

answer = 0
for i in K:
    if int(i) <= N:
        answer = max(answer, int(i))
    else:
        print(answer)
        sys.exit()

j = 2
while True:
    for p in product(K, repeat=j):
        num = "".join(map(str, p))
        if int(num) <= N:
            answer = max(answer, int(num))
        else:
            print(answer)
            sys.exit()

    j += 1
