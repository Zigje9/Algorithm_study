import sys
sys.setrecursionlimit(10**6)

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

N = len(S)


def dfs(now_t):
    if len(now_t) == N:
        if now_t == S:
            print(1)
            sys.exit()
        else:
            return

    if now_t[-1] == "A":
        dfs(now_t[:-1])

    if now_t[0] == "B":
        dfs(now_t[1:][::-1])

    return


dfs(T)

print(0)
