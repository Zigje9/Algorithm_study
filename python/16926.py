import sys

N, M, R = map(int, sys.stdin.readline().split())

line = min(N, M) // 2

matrix = [[0 for _ in range(M+1)]]

for _ in range(N):
    matrix.append([0] + list(map(int, sys.stdin.readline().split())))

mini_matrix = []


def get_mini_matrix(x, y, N, M):
    right_stack = M-(x-1)*2-1
    down_stack = N-(x-1)*2-1
    left_stack = M-(x-1)*2-1
    up_stack = N-(x-1)*2-2
    now_direction = "right"
    mini = []
    mini.append(matrix[x][y])
    while True > 0:
        if now_direction == "right":
            if right_stack > 0:
                y += 1
                right_stack -= 1
                mini.append(matrix[x][y])
            else:
                now_direction = "down"
        elif now_direction == "down":
            if down_stack > 0:
                x += 1
                down_stack -= 1
                mini.append(matrix[x][y])
            else:
                now_direction = "left"
        elif now_direction == "left":
            if left_stack > 0:
                y -= 1
                left_stack -= 1
                mini.append(matrix[x][y])
            else:
                now_direction = "up"
        else:
            if up_stack > 0:
                x -= 1
                up_stack -= 1
                mini.append(matrix[x][y])
            else:
                break
    return mini


def write_matrix(x, y, arr, N, M):
    right_stack = M-(x-1)*2-1
    down_stack = N-(x-1)*2-1
    left_stack = M-(x-1)*2-1
    up_stack = N-(x-1)*2-2
    now_direction = "right"
    matrix[x][y] = arr[0]
    k = 1
    while True > 0:
        if now_direction == "right":
            if right_stack > 0:
                y += 1
                right_stack -= 1
                matrix[x][y] = arr[k]
                k += 1
            else:
                now_direction = "down"
        elif now_direction == "down":
            if down_stack > 0:
                x += 1
                down_stack -= 1
                matrix[x][y] = arr[k]
                k += 1
            else:
                now_direction = "left"
        elif now_direction == "left":
            if left_stack > 0:
                y -= 1
                left_stack -= 1
                matrix[x][y] = arr[k]
                k += 1
            else:
                now_direction = "up"
        else:
            if up_stack > 0:
                x -= 1
                up_stack -= 1
                matrix[x][y] = arr[k]
                k += 1
            else:
                break


for i in range(line):
    temp_matrix = get_mini_matrix(i+1, i+1, N, M)
    if len(temp_matrix) > R:
        temp_matrix = temp_matrix[R:] + temp_matrix[:R]
    if len(temp_matrix) < R:
        temp_matrix = temp_matrix[R % len(
            temp_matrix):] + temp_matrix[:R % len(temp_matrix)]
    mini_matrix.append(temp_matrix)

for i in range(line):
    write_matrix(i+1, i+1, mini_matrix[i], N, M)

for i in range(1, N+1):
    print(" ".join(map(str, matrix[i][1:])))
