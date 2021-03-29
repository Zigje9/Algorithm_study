import sys

N, K = map(int, sys.stdin.readline().split())

numbers = [1] * (N+1)

answer = 0
count = 0
for i in range(2, N+1):
    if numbers[i] == 1:
        count += 1
        if count == K:
            print(i)
            sys.exit()
        for j in range(2*i, N+1, i):
            if numbers[j] == 1:
                numbers[j] = 0
                count += 1
                if count == K:
                    print(j)
                    sys.exit()
