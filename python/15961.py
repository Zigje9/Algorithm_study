# PyPy3 로 통과
import sys

N, d, k, c = map(int, sys.stdin.readline().split())

num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

nums = num_list*2

check = {}

answer = 0
for i in range(k):
    if nums[i] in check:
        check[nums[i]] += 1
    else:
        check[nums[i]] = 1
        answer += 1

first_flag = False
if c not in check:
    first_flag = True
    answer += 1

if answer == k+1:
    print(answer)
    sys.exit()

if first_flag:
    answer -= 1

i = 0
temp = answer
result = answer
for j in range(k, 2*N):
    check[nums[i]] -= 1
    if check[nums[i]] == 0:
        temp -= 1
    i += 1

    if nums[j] in check:
        if check[nums[j]] == 0:
            temp += 1
        check[nums[j]] += 1
    else:
        check[nums[j]] = 1
        temp += 1

    flag = False
    if c in check:
        if check[c] == 0:
            temp += 1
            flag = True
    else:
        temp += 1
        flag = True

    result = max(temp, result)
    if result == k+1:
        print(result)
        sys.exit()

    if flag:
        temp -= 1

print(result)
