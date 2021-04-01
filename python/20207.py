import sys

N = int(sys.stdin.readline())

check = [0]*367


schedule = []
for _ in range(N):
    schedule.append(list(map(int, sys.stdin.readline().split())))

s_schedule = sorted(schedule, key=lambda x: (x[0], -x[1]))


def fill_schedule(arr):
    left, right = arr[0], arr[1]
    for i in range(left, right+1):
        check[i] += 1


for day in s_schedule:
    fill_schedule(day)

width = 0
height = 0
answer = 0
for i in range(len(check)):
    if check[i] != 0:
        width += 1
        height = max(height, check[i])
    else:
        if width > 0:
            answer += width * height
            width = 0
            height = 0

print(answer)
