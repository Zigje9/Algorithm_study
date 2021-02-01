import sys
S = sys.stdin.readline().rstrip()

def solution(S):
    flag = 0
    stack = []
    answer = ""
    for char in S:
        if char == "<":
            flag = 1
            while len(stack) != 0 :
                answer += stack.pop()
            answer += char
            continue
        if char == ">":
            flag = 0
            answer += char
            continue
        if char == " ":
            if flag == 1:
                answer += char
                continue
            else:
                while len(stack) != 0 :
                    answer += stack.pop()
                answer += char
                continue
        if flag == 0:
            stack.append(char)
            continue
        answer += char
    while len(stack) != 0:
        answer += stack.pop()
    print(answer)
solution(S)