import sys

sys.setrecursionlimit(10**7)

T = int(sys.stdin.readline())


def dfs(num_list, cycle, result, start):
    result[start] = 1
    after = num_list[start]
    if result[after] == 1:
        if after in cycle:
            return cycle[cycle.index(after):]
        return
    else:
        cycle.append(after)
        return dfs(num_list, cycle, result, after)


def solution():
    N = int(sys.stdin.readline())
    people = [0] + list(map(int, sys.stdin.readline().split()))
    result = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if result[i] == 0:
            temp = [i]
            cycle = dfs(people, temp, result, i)
            if cycle:
                cnt += len(cycle)

    print(N-cnt)


while T > 0:
    solution()
    T -= 1
