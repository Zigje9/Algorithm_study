import sys

N, K = map(int, sys.stdin.readline().split())

number = list(map(str, sys.stdin.readline().rstrip()))

stack = []
count = 0
for idx, num in enumerate(number):
    if len(stack) == 0:
        stack.append(num)
        continue
    if count == K:
        if idx <= len(number) - 1:
            while idx <= len(number)-1:
                stack.append(number[idx])
                idx += 1
        break
    if stack[-1] < num:
        stack.append(num)
        while len(stack) > 1:
            if count == K:
                break
            if stack[-2] < stack[-1]:
                temp = stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(temp)
                count += 1
            else:
                break
    else:
        stack.append(num)

if count < K:
    stack = stack[:-(K-count)]

print("".join(stack))
