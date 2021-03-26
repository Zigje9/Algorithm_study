import sys

N = int(sys.stdin.readline())

people = []
for _ in range(N):
    people.append(int(sys.stdin.readline()))

answer = 0
people.sort(reverse=True)
rank = 1
for idx, tip in enumerate(people):
    money = tip - (idx+1) + 1
    if money < 0:
        break
    answer += money

print(answer)
