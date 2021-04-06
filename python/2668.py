import sys

N = int(sys.stdin.readline())

visit = [0] * (N+1)

num = ["X"]
for _ in range(N):
    num.append(int(sys.stdin.readline()))


def dfs(start, now, cycle):
    if visit[now] == 1:
        return -1

    if visit[num[now]] == 1:
        return -1

    cycle[now] = 1

    if num[now] == start:
        for i in range(1, N+1):
            if cycle[i] == 1:
                visit[i] = 1
        return
    else:
        if cycle[num[now]] == 1:
            return
        if num[now] == now:
            return
        dfs(start, num[now], cycle)


for i in range(1, N+1):
    if visit[i] == 0:
        cycle_visit = [0] * (N+1)
        dfs(i, i, cycle_visit)

total = sum(visit)
if total == 0:
    print(0)
else:
    print(total)
    n = 1
    while total > 0:
        if visit[n] == 1:
            print(n)
            total -= 1
        n += 1
