# D, S, L, R
# D -> N * 2 이거나 10000보다 크면 2*N mod 10000 결과
# S -> N-1 이거나 0 이라면 9999
# L -> << 시프트
# R -> >> 시프트

# 시도중 #

import sys
t = int(sys.stdin.readline())
answer = ""
while t > 0:
    A, B = map(int, sys.stdin.readline().split())
    answer += "P"
    t -= 1