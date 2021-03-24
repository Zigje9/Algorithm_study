import sys

N, M = map(int, sys.stdin.readline().split())

s_list = []

for _ in range(N):
    s_list.append(str(sys.stdin.readline().rstrip()))

S = set(s_list)

answer = 0

for _ in range(M):
    temp_str = str(sys.stdin.readline().rstrip())
    if temp_str in S:
        answer += 1

print(answer)
