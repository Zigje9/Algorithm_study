import sys
N, M = map(int, sys.stdin.readline().split())
num_line = sys.stdin.readline()
num_arr = sorted(list(map(int, num_line.split())))
visit = []
for i in range(N):
    visit.append(0)


def dfs(count, answer):
    if count == 0:
        print(' '.join(answer))
        return
    for idx in range(N):
        if visit[idx] == 0:
            visit[idx] = 1
            answer.append(str(num_arr[idx]))
            dfs(count-1, answer)
            answer.pop()
            visit[idx] = 0

dfs(M, [])

