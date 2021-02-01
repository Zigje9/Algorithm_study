import sys


def dfs(length, numbers, visit, count, answer):
    if count == 6:
        print(" ".join(map(str, answer)))
        return
    for i in range(length):
        if visit[i] == 0:
            if len(answer) != 0:
                if answer[-1] < numbers[i]:
                    visit[i] = 1
                    answer.append(numbers[i])
                    count += 1
                    dfs(length, numbers, visit, count, answer)
                    count -= 1
                    visit[i] = 0
                    answer.pop()
            else:
                visit[i] = 1
                answer.append(numbers[i])
                count += 1
                dfs(length, numbers, visit, count, answer)
                count -= 1
                visit[i] = 0
                answer.pop()


while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    length = numbers[0]
    if length == 0:
        break
    visit = []
    for i in range(length):
        visit.append(0)
    dfs(length, numbers[1:], visit, 0, [])
    print()
