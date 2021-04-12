import sys
from itertools import permutations

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

num_list = []
for _ in range(N):
    num_list.append(str(sys.stdin.readline().rstrip()))

card = {}

for com in permutations(num_list, K):
    temp_str = "".join(com)
    if temp_str not in card:
        card[temp_str] = True

print(len(card))
