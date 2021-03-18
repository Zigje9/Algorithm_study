import sys

N = int(sys.stdin.readline())

TOP = list(map(int, sys.stdin.readline().split()))

Stack = [[TOP[0], 1]]
result = [0]
for i in range(1, N):
    now_value = TOP[i]
    now_idx = i+1
    while True:
        if len(Stack) == 0:
            Stack.append([now_value, now_idx])
            result.append(0)
            break
        if Stack[-1][0] < now_value:
            Stack.pop(-1)
        else:
            result.append(Stack[-1][1])
            Stack.append([now_value, now_idx])
            break

print(" ".join(map(str, result)))
