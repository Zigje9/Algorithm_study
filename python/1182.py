import sys
sys.setrecursionlimit(10**7)
N, S = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

answer = 0


def dfs(now_idx, value):
    global answer
    if now_idx == N:
        return

    if value + num_list[now_idx] == S:
        answer += 1

    dfs(now_idx+1, value+num_list[now_idx])
    dfs(now_idx+1, value)


dfs(0, 0)

print(answer)
