import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

DP = [[0]*21 for _ in range(N+1)]

DP[0][num_list[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if DP[i-1][j] > 0:
            if j + num_list[i] <= 20:
                DP[i][j+num_list[i]] += DP[i-1][j]
            if j - num_list[i] >= 0:
                DP[i][j-num_list[i]] += DP[i-1][j]

print(DP[N-2][num_list[-1]])

# DP[i][j] => i번째 숫자까지 연산시 j가 나오는 개수
