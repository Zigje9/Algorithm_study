import sys


def lps(P, N):
    lps_array = [0] * N
    j = 0
    i = 1
    while i < N:
        if P[i] == P[j]:
            j += 1
            lps_array[i] = j
            i += 1
        else:
            if j == 0:
                lps_array[i] = 0
                i += 1
            else:
                j = lps_array[j-1]
    return lps_array[N-1]


while True:
    P = sys.stdin.readline().rstrip()

    if P == ".":
        break

    N = len(P)

    result = lps(P, N)

    K = N - result
    if K == 0:
        print(1)
    else:
        if N % K == 0:
            print(N // K)
        else:
            print(1)
