import sys

N = int(sys.stdin.readline())

gym = list(map(int, sys.stdin.readline().split()))

gym.sort()

protein = 0
if N % 2 != 0:
    protein = gym[N-1]
    gym = gym[:N-1]
    N -= 1

start = 0
end = N-1
while start < end:
    if gym[start] + gym[end] > protein:
        protein = gym[start] + gym[end]
    start += 1
    end -= 1

print(protein)
