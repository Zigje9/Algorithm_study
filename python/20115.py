import sys

N = int(sys.stdin.readline())

energy = sorted(list(map(int, sys.stdin.readline().split())), key=lambda x: -x)

print(energy[0] + sum(energy[1:])/2)
