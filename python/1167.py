import sys
N = int(sys.stdin.readline())

relation_map_list = []
for i in range(N+1):
    relation_map_list.append({})

for idx in range(1, N+1):
    line = list(map(int, sys.stdin.readline().split()))
    line = line[1:-1]
