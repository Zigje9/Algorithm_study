import sys

N = int(sys.stdin.readline())

coding = sorted(list(map(int, sys.stdin.readline().split())))

answer = 0

for i in range(N-2):
    choice_value = coding[i]

    if choice_value > 0:
        break

    left = i + 1
    right = N - 1

    while left < right:
        value = choice_value + coding[left] + coding[right]

        if value == 0:
            if coding[left] == coding[right]:
                answer += (right-left+1)*(right-left)//2
                break
            else:
                is_right = coding[right]
                r = 0
                while True:
                    if coding[right] != is_right:
                        break
                    else:
                        right -= 1
                        r += 1

                is_left = coding[left]
                l = 0
                while True:
                    if coding[left] != is_left:
                        break
                    else:
                        left += 1
                        l += 1
                answer += l*r

        elif value > 0:
            right -= 1

        else:
            left += 1

print(answer)
