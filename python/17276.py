import sys

T = int(sys.stdin.readline())


def solution():
    N, d = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(N+1)]]
    for _ in range(N):
        matrix.append([0] + list(map(int, sys.stdin.readline().split())))
    if d < 0:
        d = d+360
    line = N // 2
    center = N // 2 + 1

    locations = [[] for _ in range(8)]
    for i in range(1, line+1):
        locations[0].append([center, i])
        locations[4].append([center, 2*center-i])

        locations[1].append([i, i])
        locations[5].append([2*center-i, 2*center-i])

        locations[2].append([i, center])
        locations[6].append([2*center-i, center])

        locations[3].append([i, 2*center-i])
        locations[7].append([2*center-i, i])

    values = [[] for _ in range(8)]
    for i in range(8):
        for j in range(line):
            values[i].append(matrix[locations[i][j][0]][locations[i][j][1]])

    rotations = 8 - d // 45
    values = values[rotations:] + values[:rotations]
    for i in range(8):
        for j in range(line):
            matrix[locations[i][j][0]][locations[i][j][1]] = values[i][j]

    for i in range(1, N+1):
        print(" ".join(map(str, matrix[i][1:])))


while T > 0:
    solution()
    T -= 1
