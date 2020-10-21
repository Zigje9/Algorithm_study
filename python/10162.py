import sys
N = int(sys.stdin.readline())
A = 300
B = 60
C = 10
answer = [0, 0, 0]


def change(T):
    answer[0] += (T // A)
    T = T % A
    answer[1] += (T // B)
    T = T % B
    answer[2] += (T // C)
    T = T % C
    return T


if change(N) == 0:
    print(answer[0], answer[1], answer[2])
else:
    print(-1)
