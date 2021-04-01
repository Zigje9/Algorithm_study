import sys
from itertools import combinations

numbers = list(str(sys.stdin.readline().rstrip()))

answer = []


def get_combinations(length):
    return list(combinations([i+1 for i in range(length)], 2))


def recur(num_array, result):
    if len(num_array) == 1:
        if int(num_array[0]) % 2 != 0:
            result += 1
        answer.append(result)
        return
    elif len(num_array) == 2:
        if int(num_array[0]) % 2 != 0:
            result += 1
        if int(num_array[1]) % 2 != 0:
            result += 1
        new_num = str(int(num_array[0]) + int(num_array[1]))
        recur(new_num, result)
    else:
        for num in num_array:
            if int(num) % 2 != 0:
                result += 1
        for com in get_combinations(len(num_array)-1):
            recur(list(map(str, str(int("".join(num_array[:com[0]])) +
                                    int("".join(num_array[com[0]:com[1]])) +
                                    int("".join(num_array[com[1]:]))))), result)


recur(numbers, 0)

print(min(answer), max(answer))
