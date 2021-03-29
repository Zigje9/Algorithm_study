import sys
from collections import deque
from itertools import combinations

exp = list(sys.stdin.readline().rstrip())

stack = deque()
pair = []

answer = []

for idx, val in enumerate(exp):
    if val == "(":
        stack.append(idx)
        continue
    if val == ")":
        left = stack.pop()
        pair.append([left, idx])
        continue

all_combination = []

for v in pair:
    left, right = v
    answer.append("".join(exp[:left] + exp[left+1:right] + exp[right+1:]))

for i in range(2, len(pair)+1):
    all_combination.append(list(combinations(pair, i)))


def flat(arr):
    flatten = []
    for i in arr:
        flatten += i
    return flatten


for C in all_combination:
    for CC in C:
        f = flat(CC)
        temp_str = ""
        for i in range(len(exp)):
            if i not in f:
                temp_str += exp[i]
        answer.append(temp_str)

answer = list(set(answer))
answer.sort()

for a in answer:
    print(a)
