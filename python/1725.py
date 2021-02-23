import sys
from collections import deque

N = int(sys.stdin.readline())

histogram = [0]
for _ in range(N):
    histogram.append(int(sys.stdin.readline()))


def solution():
    answer = 0
    S = deque()
    S.append(0)
    histogram.append(0)
    for i in range(1, N+2):
        while len(S) > 0 and histogram[S[-1]] > histogram[i]:
            height = histogram[S[-1]]
            S.pop()
            width = i-S[-1]-1
            answer = max(answer, height*width)
        S.append(i)
    print(answer)


solution()
