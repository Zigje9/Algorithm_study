import sys
from itertools import combinations

find = sys.stdin.readline().rstrip()

N = int(sys.stdin.readline())

book = []

answer = 2e9

for _ in range(N):
    money, name = sys.stdin.readline().split()
    book.append([int(money), name])

for m, s in book:  # 한개씩 검사
    if answer < m:
        continue

    temp = {}
    for c in s:
        if c in temp:
            temp[c] += 1
        else:
            temp[c] = 1

    flag = True
    for check in find:
        if check not in temp:
            flag = False
            break

        if temp[check] == 0:
            flag = False
            break

        temp[check] -= 1

    if flag:
        answer = min(answer, m)

for j in range(2, N+1):
    for com in combinations(book, j):
        temp_money = 0
        for k in range(j):
            temp_money += com[k][0]
        if answer < temp_money:
            continue

        temp = {}
        for k in range(j):
            for c in com[k][1]:
                if c in temp:
                    temp[c] += 1
                else:
                    temp[c] = 1

        flag = True
        for check in find:
            if check not in temp:
                flag = False
                break

            if temp[check] == 0:
                flag = False
                break

            temp[check] -= 1

        if flag:
            answer = min(answer, temp_money)

if answer == 2e9:
    print(-1)
else:
    print(answer)
