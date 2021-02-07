import sys
N = int(input())


answer = []


def check_palindrome(palin):
    left_idx = 0
    right_idx = len(palin)-1
    l_chance = 1
    r_chance = 1
    l_result = 0
    r_result = 0
    while left_idx <= right_idx:
        if palin[left_idx] == palin[right_idx]:
            left_idx += 1
            right_idx -= 1
        else:
            if l_chance == 1:
                l_chance -= 1
                left_idx += 1
            else:
                l_result = 2
                break
    if l_result == 0 and l_chance == 0:
        l_result = 1

    if l_result == 0 or l_result == 1:
        return l_result

    left_idx = 0
    right_idx = len(palin)-1

    while left_idx <= right_idx:
        if palin[left_idx] == palin[right_idx]:
            left_idx += 1
            right_idx -= 1
        else:
            if r_chance == 1:
                r_chance -= 1
                right_idx -= 1
            else:
                r_result = 2
                break
    if r_result == 0 and r_chance == 0:
        r_result = 1

    return r_result


for i in range(N):
    answer.append(check_palindrome(sys.stdin.readline().rstrip()))

for a in answer:
    print(a)
