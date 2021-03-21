import sys

N, P = map(int, sys.stdin.readline().split())

stacks = [[] for _ in range(N+1)]

answer = 0

for _ in range(N):
    L, P = map(int, sys.stdin.readline().split())
    if len(stacks[L]) == 0:
        stacks[L].append(P)
        answer += 1
    else:
        while True:
            if len(stacks[L]) == 0:
                stacks[L].append(P)
                answer += 1
                break
            if P > stacks[L][-1]:
                stacks[L].append(P)
                answer += 1
                break
            if P == stacks[L][-1]:
                break
            if P < stacks[L][-1]:
                stacks[L].pop(-1)
                answer += 1

print(answer)
