import sys

N = int(sys.stdin.readline())

for i in range(1, N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        sys.exit()

print(0)
