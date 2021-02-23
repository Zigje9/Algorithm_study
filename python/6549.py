import sys
from collections import deque


def solution(input_array):
    histogram = [0]
    N = len(input_array) - 1
    histogram = histogram + input_array[1:]
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


while True:
    input_array = list(map(int, sys.stdin.readline().split()))
    if input_array[0] == 0:
        break
    solution(input_array)
