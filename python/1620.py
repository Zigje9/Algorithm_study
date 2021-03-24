import sys

N, M = map(int, sys.stdin.readline().split())

poket = {}
poket_number = [0]
for i in range(1, N+1):
    p = str(sys.stdin.readline().rstrip())
    poket_number.append(p)
    poket[p] = i

for j in range(M):
    answer = str(sys.stdin.readline().rstrip())
    if answer.isdigit():
        print(poket_number[int(answer)])
    else:
        print(poket[answer])
