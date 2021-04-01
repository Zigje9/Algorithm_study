import sys

T = int(sys.stdin.readline())


def solution():
    line = sys.stdin.readline().replace(" ", "").rstrip()
    alpha = {}
    for word in line:
        if word in alpha:
            alpha[word] += 1
        else:
            alpha[word] = 1
    temp = []
    for key, value in alpha.items():
        temp.append([key, value])

    answer = sorted(temp, key=lambda x: (-x[1]))
    if len(answer) == 1:
        print(answer[0][0])
    else:
        if answer[0][1] == answer[1][1]:
            print("?")
        else:
            print(answer[0][0])


while T > 0:
    solution()
    T -= 1
