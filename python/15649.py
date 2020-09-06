import sys
N, M = map(int, sys.stdin.readline().split())

num_list = []
visit = [0]

for i in range(1, N+1):
    num_list.append(i)
    visit.append(0)

answer = []


def dfs(next, count, answer):
    if count == 0:
        output = list(map(str, answer))
        print(" ".join(output))
        return
    else:
        for next in num_list:
            if visit[next] == 0:
                visit[next] = 1
                answer.append(next)
                dfs(next, count-1, answer)
                answer.pop(-1)
                visit[next] = 0

dfs(0, M, answer)


