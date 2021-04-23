import sys

N = int(sys.stdin.readline())

money = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())


def check(now):
    temp = 0
    for a in money:
        if a < now:
            temp += a
        else:
            temp += now
    return temp


left = 0
right = max(money)
answer = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid) > M:
        right = mid - 1
    else:
        answer = max(answer, mid)
        left = mid + 1

print(answer)
