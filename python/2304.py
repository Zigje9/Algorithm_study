import sys

N = int(sys.stdin.readline())

stick = []
for _ in range(N):
    stick.append(list(map(int, sys.stdin.readline().split())))

stick.sort()

answer = 0
if N == 1:
    print(stick[0][1])
else:
    left_stick = stick[0][1]
    left_idx = stick[0][0]
    idx = 1
    while idx <= len(stick)-1:
        if stick[idx][1] >= left_stick:
            answer += (stick[idx][0]-left_idx)*left_stick
            left_stick = stick[idx][1]
            left_idx = stick[idx][0]
        idx += 1

    right_stick = stick[-1][1]
    right_idx = stick[-1][0]
    r_idx = len(stick)-2
    while r_idx >= 0:
        if stick[r_idx][1] == left_stick:
            answer += (right_idx-left_idx)*right_stick
            break
        if stick[r_idx][1] >= right_stick:
            answer += (right_idx-stick[r_idx][0])*right_stick
            right_stick = stick[r_idx][1]
            right_idx = stick[r_idx][0]
        r_idx -= 1

    answer += left_stick
    print(answer)
