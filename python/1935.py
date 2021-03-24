import sys
from collections import deque

numbers = []

N = int(sys.stdin.readline())

operator = ["+", "-", "/", "*"]

stack = deque()

expression = list(map(str, sys.stdin.readline().rstrip()))


def calculate(exp, val1, val2):
    if exp == "+":
        return val1+val2
    if exp == "-":
        return val1-val2
    if exp == "/":
        return val1/val2
    if exp == "*":
        return val1*val2


for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

for i in range(len(expression)):
    if expression[i] in operator:
        val1 = stack[-2]
        val2 = stack[-1]
        stack.pop()
        stack.pop()
        stack.append(calculate(expression[i], val1, val2))
    else:
        stack.append(numbers[ord(expression[i])-65])

print(format(stack[0], ".2f"))
