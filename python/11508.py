import sys

N = int(sys.stdin.readline())

items = []

for _ in range(N):
    items.append(int(sys.stdin.readline()))

items.sort(reverse=True)

answer = sum(items)

for i in range(2, N, 3):
    answer -= items[i]

print(answer)
