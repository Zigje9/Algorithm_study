import sys
from itertools import permutations

T = int(sys.stdin.readline())

answer = 0

try_list = []
for _ in range(T):
    try_list.append(list(map(int, sys.stdin.readline().split())))

baseball = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for game in list(permutations(baseball, 3)):
    first = game[0]
    second = game[1]
    third = game[2]
    flag = 0
    for num in try_list:
        strike = 0
        ball = 0
        a = str(num[0])[0]
        b = str(num[0])[1]
        c = str(num[0])[2]
        if first in [a, b, c]:
            if first == a:
                strike += 1
            else:
                ball += 1

        if second in [a, b, c]:
            if second == b:
                strike += 1
            else:
                ball += 1

        if third in [a, b, c]:
            if third == c:
                strike += 1
            else:
                ball += 1

        if strike == num[1] and ball == num[2]:
            flag += 1
        else:
            break
    if flag == len(try_list):
        answer += 1

print(answer)
