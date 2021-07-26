import sys

N = int(sys.stdin.readline())

city = []
total = 0
for _ in range(N):
    num, people = map(int, sys.stdin.readline().split())
    total += people
    city.append([num, people])

city.sort()
acc = 0
for c, v  in city:
    acc += v
    if acc*2 >= total:
        print(c)
        break

