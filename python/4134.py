import sys

T = int(sys.stdin.readline())

M = 65000
numbers = [1] * (M)
numbers[1] = 0
prime = []

for i in range(2, M):
    if numbers[i] == 1:
        prime.append(i)
        for j in range(2*i, M, i):
            numbers[j] = 0


def solution():
    N = int(sys.stdin.readline())
    if N == 1 or N == 0:
        print(2)
        return
    while True:
        sqrt_N = int(N ** 0.5)
        flag = False
        for num in prime:
            if sqrt_N < num:
                flag = True
                break
            if N % num == 0:
                flag = False
                break
        if flag:
            print(N)
            break
        else:
            N += 1


while T > 0:
    solution()
    T -= 1
