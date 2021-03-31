import sys

N = int(sys.stdin.readline())

files = {}

for _ in range(N):
    _, f = str(sys.stdin.readline().rstrip()).split(".")
    if f in files:
        files[f] += 1
    else:
        files[f] = 1

answer = []
for key, value in files.items():
    answer.append([key, value])
answer.sort()
for name in answer:
    print(name[0], name[1])
