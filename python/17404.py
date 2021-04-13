import sys

N = int(sys.stdin.readline())

DATA = [[0]*4]

for _ in range(N):
    DATA.append([0] + list(map(int, sys.stdin.readline().split())))

DP1 = [[0]*4 for _ in range(N+1)]
DP2 = [[0]*4 for _ in range(N+1)]
DP3 = [[0]*4 for _ in range(N+1)]

DP1[1][1] = DATA[1][1]
DP1[1][2] = 2e9
DP1[1][3] = 2e9
DP1[2][1] = 2e9
DP1[2][2] = DATA[2][2] + DP1[1][1]
DP1[2][3] = DATA[2][3] + DP1[1][1]

DP2[1][2] = DATA[1][2]
DP2[1][1] = 2e9
DP2[1][3] = 2e9
DP2[2][2] = 2e9
DP2[2][1] = DATA[2][1] + DP2[1][2]
DP2[2][3] = DATA[2][3] + DP2[1][2]

DP3[1][3] = DATA[1][3]
DP3[1][1] = 2e9
DP3[1][2] = 2e9
DP3[2][3] = 2e9
DP3[2][1] = DATA[2][1] + DP3[1][3]
DP3[2][2] = DATA[2][2] + DP3[1][3]

for i in range(3, N):
    DP1[i][1] = DATA[i][1] + min(DP1[i-1][2], DP1[i-1][3])
    DP1[i][2] = DATA[i][2] + min(DP1[i-1][1], DP1[i-1][3])
    DP1[i][3] = DATA[i][3] + min(DP1[i-1][1], DP1[i-1][2])

for i in range(1, 4):
    DP2[1][i] = DATA[1][i]

for i in range(3, N):
    DP2[i][1] = DATA[i][1] + min(DP2[i-1][2], DP2[i-1][3])
    DP2[i][2] = DATA[i][2] + min(DP2[i-1][1], DP2[i-1][3])
    DP2[i][3] = DATA[i][3] + min(DP2[i-1][1], DP2[i-1][2])

for i in range(1, 4):
    DP3[1][i] = DATA[1][i]

for i in range(3, N):
    DP3[i][1] = DATA[i][1] + min(DP3[i-1][2], DP3[i-1][3])
    DP3[i][2] = DATA[i][2] + min(DP3[i-1][1], DP3[i-1][3])
    DP3[i][3] = DATA[i][3] + min(DP3[i-1][1], DP3[i-1][2])

DP1[N][2] = DATA[N][2] + min(DP1[N-1][1], DP1[N-1][3])
DP1[N][3] = DATA[N][3] + min(DP1[N-1][1], DP1[N-1][2])

DP2[N][1] = DATA[N][1] + min(DP2[N-1][2], DP2[N-1][3])
DP2[N][3] = DATA[N][3] + min(DP2[N-1][1], DP2[N-1][2])

DP3[N][1] = DATA[N][1] + min(DP3[N-1][2], DP3[N-1][3])
DP3[N][2] = DATA[N][2] + min(DP3[N-1][1], DP3[N-1][3])

print(min(DP1[N][2], DP1[N][3], DP2[N][1], DP2[N][3], DP3[N][1], DP3[N][2]))
