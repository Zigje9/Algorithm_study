import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    di = {}
    for _ in range(N):
        for num in list(map(int, sys.stdin.readline().split())):
            if num in di:
                di[num] += 1
            else:
                di[num] = 1

    temp = sorted(di.items(), key=lambda x: -x[1])
    max_num = temp[1][1]
    answer = []
    for tp in temp[1:]:
        if tp[1] == max_num:
            answer.append(tp[0])
        else:
            break
    answer.sort()
    print(" ".join(map(str, answer)))
