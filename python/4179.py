import sys

N, M = map(int, sys.stdin.readline().split())

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

board = []

visit_J = [[0]*M for _ in range(N)]
visit_F = [[0]*M for _ in range(N)]

for _ in range(N):
    board.append(list(map(str, sys.stdin.readline().rstrip())))

for j in range(M):
    if board[0][j] == "J":
        print(1)
        sys.exit()

for j in range(M):
    if board[N-1][j] == "J":
        print(1)
        sys.exit()

for i in range(1, N-1):
    if board[i][0] == "J":
        print(1)
        sys.exit()

for i in range(1, N-1):
    if board[i][M-1] == "J":
        print(1)
        sys.exit()


def move_F(x, y):
    pos = []
    for i in range(4):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if 0 <= next_x < N and 0 <= next_y < M and visit_F[next_x][next_y] == 0:
            if board[next_x][next_y] == "J" or board[next_x][next_y] == ".":
                visit_F[next_x][next_y] = 1
                board[next_x][next_y] = "F"
                pos.append([next_x, next_y])
    return pos


def move_J(x, y):
    pos = []
    for i in range(4):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if 0 <= next_x < N and 0 <= next_y < M and visit_J[next_x][next_y] == 0:
            if board[next_x][next_y] == ".":
                visit_J[next_x][next_y] = 1
                board[next_x][next_y] = "J"
                pos.append([next_x, next_y])
    return pos


def get_first():
    pos_J = []
    pos_F = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == "J":
                pos_J.append([i, j])
                visit_J[i][j] = 1
                continue
            if board[i][j] == "F":
                pos_F.append([i, j])
                visit_F[i][j] = 1
    return [pos_J, pos_F]


def check_lines(t):
    count = 0
    for j in range(M):
        if board[0][j] == "J":
            print(t + 1)
            sys.exit()
        if board[0][j] != ".":
            count += 1

    for j in range(M):
        if board[N-1][j] == "J":
            print(t + 1)
            sys.exit()
        if board[N-1][j] != ".":
            count += 1

    for i in range(1, N-1):
        if board[i][0] == "J":
            print(t + 1)
            sys.exit()
        if board[i][0] != ".":
            count += 1

    for i in range(1, N-1):
        if board[i][M-1] == "J":
            print(t + 1)
            sys.exit()
        if board[i][M-1] != ".":
            count += 1
    if count == (N+M)*2-4:
        print("IMPOSSIBLE")
        sys.exit()


next_pos_J, next_pos_F = get_first()


time = 1
while True:
    if len(next_pos_J) == 0:
        print("IMPOSSIBLE")
        sys.exit()

    now_pos_J = next_pos_J[:]
    next_pos_J = []
    for x, y in now_pos_J:
        next_pos_J += move_J(x, y)

    now_pos_F = next_pos_F[:]
    next_pos_F = []
    for x, y in now_pos_F:
        next_pos_F += move_F(x, y)

    check_lines(time)
    time += 1
