import sys

N, X = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

answer = []

for ele in num_list:
  if ele < X:
    answer.append(ele)

print(" ".join(map(str, answer)))


