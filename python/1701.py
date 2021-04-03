import sys

P = sys.stdin.readline().rstrip()


def lps(P):
    N = len(P)
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
    return max(lps_array)


answer = 0
for i in range(len(P)):
    answer = max(answer, lps(P[i:]))


print(answer)
