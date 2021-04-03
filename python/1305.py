import sys

L = int(sys.stdin.readline())

P = sys.stdin.readline().rstrip()


def lps(P):
    N = len(P)
    lps_array = [0] * N
    i = 1
    j = 0
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


print(L - lps(P))
