import sys

N = int(sys.stdin.readline())

if N == 1:
    print("*")
    sys.exit()

M = 4*(N-1)+1

stack = []

for i in range(M // 2):
    temp = []
    for j in range(M):
        if i % 2 == 0:
            temp.append("*")
        else:
            temp.append(" ")
    if i % 2 == 0:
        t = i // 2
        idx = 1
        while t > 0:
            temp[idx] = " "
            temp[-(idx+1)] = " "
            idx += 2
            t -= 1
    else:
        t = i // 2 + 1
        idx = 0
        while t > 0:
            temp[idx] = "*"
            temp[-(idx+1)] = "*"
            idx += 2
            t -= 1
    print("".join(temp))
    stack.append(temp)

center = ""
for i in range(M):
    if i % 2 == 0:
        center += "*"
    else:
        center += " "

print(center)

for i in range(len(stack)-1, -1, -1):
    print("".join(stack[i]))
