import sys

N, K = map(int, sys.stdin.readline().split())

students = list(map(int, sys.stdin.readline().split()))

diff = []

for i in range(1, N):
    diff.append(students[i]-students[i-1])

diff.sort(reverse=True)

answer = sum(diff[K-1:])

print(answer)
