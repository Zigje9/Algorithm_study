import sys
N, M = map(int, sys.stdin.readline().split())

hear = []
see = []
for i in range(N):
    hear.append(str(sys.stdin.readline().rstrip()))

for i in range(M):
    see.append(str(sys.stdin.readline().rstrip()))
answer = list(set(hear) & set(see))

print(len(answer))
answer.sort()
for ele in answer:
    print(ele)
