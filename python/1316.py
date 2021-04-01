import sys

T = int(sys.stdin.readline())


answer = 0


def solution():
    global answer
    S = sys.stdin.readline().rstrip()
    check = {}
    now = S[0]
    check[S[0]] = True
    Group = True
    for idx in range(1, len(S)):
        if S[idx] == now:
            continue
        else:
            if S[idx] in check:
                Group = False
                break
            else:
                now = S[idx]
                check[S[idx]] = True
    if Group:
        answer += 1


while T > 0:
    solution()
    T -= 1

print(answer)
