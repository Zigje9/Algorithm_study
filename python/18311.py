import sys

N, K = map(int, sys.stdin.readline().split())

step = [0] + list(map(int, sys.stdin.readline().split()))

road = [0]*(N+1)

road[1] = step[1]-1

for i in range(2, N+1):
    road[i] = road[i-1]+step[i]

road[N] += 1

max_road = road[-1]

if K > max_road:
    K = max_road*2 - K

for i in range(1, N+1):
    if K <= road[i]:
        print(i)
        sys.exit()
