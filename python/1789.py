import sys

S = int(sys.stdin.readline())

for i in range(1, S+1):
    if (i*i+i)//2 > S:
        print(i-1)
        sys.exit()
