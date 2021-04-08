import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

answer = 0
for com in list(combinations(num_list, 3)):
    value = sum(com)
    if answer <= value <= M:
        answer = value

print(answer)
