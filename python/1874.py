import sys
from collections import deque

N = int(sys.stdin.readline())

numbers = deque()
for i in range(1, N+1):
    numbers.append(i)

stack = deque()
answer = []
for i in range(N):
    now_value = int(sys.stdin.readline())
    while len(numbers) > 0:
        top_number = numbers[0]
        if top_number <= now_value:
            stack.append(numbers.popleft())
            answer.append("+")
        else:
            break

    flag = True
    if len(stack) == 0:
        answer.append("NO")
        break
    else:
        while len(stack) > 0:
            if now_value < stack[-1]:
                stack.pop()
                answer.append("-")
            elif now_value > stack[-1]:
                flag = False
                break
            else:
                stack.pop()
                answer.append("-")
                break
    if flag == False:
        answer.append("NO")
        break

if answer[-1] == "NO":
    print("NO")
else:
    for a in answer:
        print(a)
