import sys
from collections import deque
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
S = list(map(str, sys.stdin.readline().rstrip()))

answer = -2e9

if N == 1:
    print(S[0])
    sys.exit()


def cal(a, o, b):
    if o == "+":
        return int(a) + int(b)
    if o == "*":
        return int(a) * int(b)
    return int(a) - int(b)


def sol(s):
    i = 1
    left = int(s[0])
    while i < len(s):
        if s[i] == "*" or s[i] == "+" or s[i] == "-":
            op = s[i]
            i += 1
        else:
            if s[i] == "(":
                right = cal(s[i+1], s[i+2], s[i+3])
                left = cal(left, op, right)
                i += 5
            else:
                right = int(s[i])
                left = cal(left, op, right)
                i += 1
    return left


def dfs(ex, idx):
    global answer
    if idx == len(S)-2:
        ex.append(S[idx+1])
        answer = max(answer, sol(ex))
        return

    if idx == len(S)-4:
        t = ex[:]
        t.append(S[idx+1])
        t.append(S[idx+2])
        dfs(t, idx+2)
        ex.append("(")
        ex += S[idx+1:]
        ex.append(")")
        answer = max(answer, sol(ex))
        return

    dfs(ex + S[idx+1:idx+3], idx+2)
    dfs(ex + ["("] + S[idx+1:idx+4] + [")"] + [S[idx+4]], idx+4)


start = []
start += S[0:2]

dfs(start, 1)

print(answer)
