import sys

N = int(sys.stdin.readline())

cows = {}

count = 0

for _ in range(N):
    cow, road = map(str, sys.stdin.readline().split())
    if cow in cows:
        if cows[cow] != road:
            cows[cow] = road
            count += 1
    else:
        cows[cow] = road

print(count)
