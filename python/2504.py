import sys

brakets = list(map(str, sys.stdin.readline().rstrip()))

stack = []

for b in brakets:
    if b == ")":
        number = 0
        while True:
            if len(stack) == 0:
                print(0)
                sys.exit()
            if stack[-1] == "[":
                print(0)
                sys.exit()
            elif stack[-1] == "(":
                stack.pop()
                if number != 0:
                    stack.append(number*2)
                else:
                    stack.append(2)
                break
            else:
                number += int(stack[-1])
                stack.pop()

    elif b == "]":
        number = 0
        while True:
            if len(stack) == 0:
                print(0)
                sys.exit()
            if stack[-1] == "(":
                print(0)
                sys.exit()
            elif stack[-1] == "[":
                stack.pop()
                if number != 0:
                    stack.append(number*3)
                else:
                    stack.append(3)
                break
            else:
                number += int(stack[-1])
                stack.pop()
    else:
        stack.append(b)

if "[" in stack or "(" in stack:
    print(0)
else:
    print(sum(stack))
