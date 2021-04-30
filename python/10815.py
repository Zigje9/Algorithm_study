import sys

N = int(sys.stdin.readline())

n_dictionary = {}
for num in list(map(int, sys.stdin.readline().split())):
    if num in n_dictionary:
        continue
    n_dictionary[num] = True


M = int(sys.stdin.readline())

answer = []

for num in list(map(int, sys.stdin.readline().split())):
    if num in n_dictionary:
        answer.append('1')
    else:
        answer.append('0')

print(" ".join(answer))
