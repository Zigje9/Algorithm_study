import sys


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


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


N = int(sys.stdin.readline())

P = sys.stdin.readline().replace(" ", "").rstrip()
sys.stdin.readline()

result = lps(P, N)

K = N - result
value = 0
if K == 0:
    value = 1
else:
    if N % K == 0:
        value = N // K
    else:
        value = 1

g = gcd(value, N)
answer = str(value//g) + "/" + str(N//g)
print(answer)
