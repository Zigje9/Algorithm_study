import sys

N = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split())))

if N == 1:
    print(1)
    sys.exit()

answer = 2
for i in range(N-2):
    now_sum = num_list[i] + num_list[i+1]
    count = 2
    for j in range(i+2, N):
        if num_list[j] < now_sum:
            count += 1
        else:
            break
    answer = max(answer, count)

print(answer)
