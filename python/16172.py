import sys

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

newS = ""
for word in S:
    if word.isalpha():
        newS += word

if P in newS:
    print(1)
else:
    print(0)

# lps_array = [0] * len(P)

# answer = []


# def lps(P):
#     j = 0
#     i = 1
#     while i < len(P):
#         if P[i] == P[j]:
#             j += 1
#             lps_array[i] = j
#             i += 1
#         else:
#             if j == 0:
#                 lps_array[i] = 0
#                 i += 1
#             else:
#                 j = lps_array[j-1]


# def KMP(P, S):
#     i = 0
#     j = 0
#     while i < len(S):
#         if P[j] == S[i]:
#             i += 1
#             j += 1
#         else:
#             if j == 0:
#                 i += 1
#             else:
#                 j = lps_array[j-1]

#         if j == len(P):
#             answer.append(i-len(P))
#             return


# lps(P)
# KMP(P, newS)

# if answer == []:
#     print(0)
# else:
#     print(1)
