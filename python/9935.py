import sys

frula_list = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()

answer = []

idx = -len(boom)

if idx == -1:
    for c in frula_list:
        if c != boom:
            answer.append(c)

else:
    for c in frula_list:
        if c != boom[-1]:
            answer.append(c)
        else:
            if "".join(answer[idx+1:]) == boom[0:-1]:
                del answer[idx+1:]
            else:
                answer.append(c)

if len(answer) == 0:
    print("FRULA")
else:
    print("".join(answer))
