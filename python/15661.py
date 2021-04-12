# PyPy3 로 통과
import sys
from itertools import combinations

N = int(sys.stdin.readline())

board = [[0]*(N+1)]

for _ in range(N):
    board.append([0] + list(map(int, sys.stdin.readline().split())))

team = set()

for i in range(1, N+1):
    team.add(i)


def get_diff(A, B):
    sum_A = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            sum_A += board[A[i]][A[j]]
            sum_A += board[A[j]][A[i]]

    sum_B = 0
    for i in range(len(B)-1):
        for j in range(i+1, len(B)):
            sum_B += board[B[i]][B[j]]
            sum_B += board[B[j]][B[i]]

    return abs(sum_A-sum_B)


answer = 2e9

for j in range(2, N // 2 + 1):
    for com in combinations(team, j):
        answer = min(answer, get_diff(list(com), list(team-set(com))))

print(answer)
