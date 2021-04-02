import sys

T = int(sys.stdin.readline())


def solution():
    W = sys.stdin.readline().rstrip()
    K = int(sys.stdin.readline())

    trys = {}
    for word in W:
        if word in trys:
            trys[word] += 1
        else:
            trys[word] = 1

    check = {}
    for key, value in trys.items():
        if value >= K:
            check[key] = []

    if len(check) == 0:
        print(-1)
        return

    answer = []

    for idx, value in enumerate(W):
        if value in check:
            check[value].append(idx)

    for key, value in check.items():
        idx = K-1
        while idx < len(value):
            answer.append(value[idx]-value[idx-K+1]+1)
            idx += 1

    print(min(answer), max(answer))


while T > 0:
    solution()
    T -= 1
