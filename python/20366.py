# PyPy3로 통과
import sys

N = int(sys.stdin.readline())

snow = sorted(list(map(int, sys.stdin.readline().split())))

answer = 2e9

for i in range(N):
    for j in range(i+1, N):
        left_snowman = snow[i] + snow[j]
        left = 0
        right = N-1
        while left < right:
            if left == i or left == j:
                left += 1
                continue

            if right == i or right == j:
                right -= 1
                continue

            if answer == 0:
                print(0)
                sys.exit()

            right_snowman = snow[left] + snow[right]

            value = left_snowman - right_snowman
            answer = min(answer, abs(value))

            if value > 0:
                left += 1
            else:
                right -= 1

print(answer)
