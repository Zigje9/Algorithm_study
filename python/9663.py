N = int(input())


def check_queen(x, y, check):
    if x == 0:
        return True
    for k in range(x):
        if check[k][y] == 1:
            return False
        if x-(k+1) >= 0 and y-(k+1) >= 0:
            if check[x-(k+1)][y-(k+1)] == 1:
                return False
        if x-(k+1) >= 0 and y+(k+1) <= N-1:
            if check[x-(k+1)][y+(k+1)] == 1:
                return False
    return True


def dfs(x, y, check, answer):
    if x == N:
        answer[0] += 1
        return
    for j in range(N):
        if check_queen(x, j, check):
            check[x][j] = 1
            dfs(x+1, j, check, answer)
            check[x][j] = 0


answer = [0]
check = [[0 for _ in range(N)] for j in range(N)]
for i in range(N):
    check[0][i] = 1
    dfs(1, i, check, answer)
    check[0][i] = 0

print(answer[0])
