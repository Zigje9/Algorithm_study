import sys

N, K = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

check = {}

i = 0
answer = 1
for j in range(N):
    if num_list[j] in check:
        if check[num_list[j]] == K:
            answer = max(answer, j-i)
            while True:
                if num_list[i] == num_list[j]:
                    i += 1
                    break
                else:
                    check[num_list[i]] -= 1
                    i += 1
        else:
            check[num_list[j]] += 1
    else:
        check[num_list[j]] = 1

answer = max(answer, N-i)
print(answer)
