import sys
N, M = map(int, sys.stdin.readline().split())
num_line = sys.stdin.readline()
num_arr = sorted(list(map(int, num_line.split())))


def dfs(count, answer):
    if count == 0:
        print(' '.join(answer))
        return
    for idx in range(N):
        if len(answer) == 0:
            answer.append(str(num_arr[idx]))
            dfs(count-1, answer)
            answer.pop()
        else:
            if int(answer[-1]) <= num_arr[idx]:
                answer.append(str(num_arr[idx]))
                dfs(count - 1, answer)
                answer.pop()

dfs(M, [])
