import sys

# KMP 알고리즘

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

N = len(P)

lps_array = [0]*(N)

answer = []


def lps(P, N):
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


def KMP(S, P, lps_array):
    j = 0
    i = 0
    while i < len(S):
        if S[i] == P[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps_array[j-1]

        if j == len(P):
            answer.append(i-len(P))
            j = lps_array[j-1]


lps(P, N)
KMP(S, P, lps_array)
print(answer)
