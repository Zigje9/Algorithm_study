import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
answer = []


def dfs(val, count, operator):
    if count == N:
        answer.append(val)
        return
    if operator[0] != 0:
        operator[0] -= 1
        dfs(val+numbers[count], count+1, operator)
        operator[0] += 1
    if operator[1] != 0:
        operator[1] -= 1
        dfs(val-numbers[count], count+1, operator)
        operator[1] += 1
    if operator[2] != 0:
        operator[2] -= 1
        dfs(val*numbers[count], count+1, operator)
        operator[2] += 1
    if operator[3] != 0:
        operator[3] -= 1
        if val < 0:
            dfs((val*(-1)//numbers[count])*(-1), count+1, operator)
        else:
            dfs(val//numbers[count], count+1, operator)
        operator[3] += 1
    return


def solution():
    dfs(numbers[0], 1, operator)
    print(max(answer))
    print(min(answer))


solution()
