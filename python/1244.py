import sys

N = int(sys.stdin.readline())

switch = list(map(int, sys.stdin.readline().split()))

s_num = int(sys.stdin.readline())

play = []
for _ in range(s_num):
    play.append(list(map(int, sys.stdin.readline().split())))


def change_switch(idx):
    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0
    return


def play_boy(idx):
    k = idx
    while True:
        if idx-1 > N-1:
            return
        change_switch(idx-1)
        idx += k


def play_girl(idx):
    real_idx = idx-1
    change_switch(real_idx)
    left = real_idx-1
    right = real_idx+1
    while True:
        if left < 0 or right > N-1:
            return

        if switch[left] == switch[right]:
            change_switch(left)
            change_switch(right)
            left -= 1
            right += 1
        else:
            return


for command in play:
    if command[0] == 1:
        play_boy(command[1])
    else:
        play_girl(command[1])

if N > 20:
    T = N // 20
    if N % 20 != 0:
        T += 1
    for i in range(T):
        print(" ".join(map(str, switch[i*20:i*20+20])))

else:
    print(" ".join(map(str, switch)))
