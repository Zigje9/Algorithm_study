import sys
N, M = map(int, sys.stdin.readline().split())


num_list = []
answer = []
for i in range(1, N+1):
    num_list.append(i)


def myprint(arr):
    for i in arr:
        print(i, end=' ')


def dfs(answer, count):
    if count == 0:
        myprint(answer)
        print()
        return 0
    for ele in num_list:
        if len(answer) != 0:
            if answer[-1] <= ele:
                answer.append(ele)
                dfs(answer, count - 1)
                answer.pop(-1)
            else:
                continue
        else:
            answer.append(ele)
            dfs(answer, count-1)
            answer.pop(-1)


dfs(answer, M)