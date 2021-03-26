import sys

A, B = map(int, sys.stdin.readline().split())

count = 1
while A < B:
    if B % 10 == 1:
        B = B//10
        count += 1
    else:
        if B % 2 == 0:
            B = B//2
            count += 1
        else:
            print(-1)
            sys.exit()

if A == B:
    print(count)
else:
    print(-1)
