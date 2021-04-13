import sys
import copy
from itertools import combinations

T = int(sys.stdin.readline())

order = [1, 2, 3, 4, 5, 6, 7, 8]


def solution():

    def change(number):
        if number == 1:
            return 0
        return 1

    def rotate(n, b):
        if n == 1:
            for i in range(3):
                b[0][i] = change(b[0][i])
        elif n == 2:
            for i in range(3):
                b[1][i] = change(b[1][i])
        elif n == 3:
            for i in range(3):
                b[2][i] = change(b[2][i])
        elif n == 4:
            for i in range(3):
                b[i][0] = change(b[i][0])

        elif n == 5:
            for i in range(3):
                b[i][1] = change(b[i][1])

        elif n == 6:
            for i in range(3):
                b[i][2] = change(b[i][2])

        elif n == 7:
            for i in range(3):
                b[i][i] = change(b[i][i])

        else:
            b[0][2] = change(b[0][2])
            b[1][1] = change(b[1][1])
            b[2][0] = change(b[2][0])

        return b

    def check(b):
        temp_sum = 0
        for i in range(3):
            temp_sum += sum(b[i])
        if temp_sum == 0 or temp_sum == 9:
            return True
        return False

    board = []
    for _ in range(3):
        board.append(list(map(str, sys.stdin.readline().split())))
    for i in range(3):
        for j in range(3):
            if board[i][j] == "H":
                board[i][j] = 1
            else:
                board[i][j] = 0

    # 8!
    # deepcopy 를 이용하지 않으면 같은 주소값 참조
    if check(board):
        print(0)
        return

    for i in order:
        temp_board = copy.deepcopy(board)
        rotate(i, temp_board)
        if check(temp_board):
            print(1)
            return

    for j in range(2, 9):
        for com in combinations(order, j):
            temp_board = copy.deepcopy(board)
            for num in com:
                temp_board = rotate(num, temp_board)
                if check(temp_board):
                    print(j)
                    return
    print(-1)


while T > 0:
    solution()
    T -= 1
