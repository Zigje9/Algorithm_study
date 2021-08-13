def connectedCell(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visit = [[False]*m for _ in range(n)]
    
    move_x = [-1, 0, 1, 0, -1, -1, 1, 1]
    move_y = [0, 1, 0, -1, -1, 1, -1, 1]
    
    location = []

    def dfs(x, y, count):
        for i in range(8):
            next_x = x + move_x[i]    
            next_y = y + move_y[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if visit[next_x][next_y] == False and matrix[next_x][next_y] == 1:
                    visit[next_x][next_y] = True
                    count = dfs(next_x, next_y, count+1)
        return count

    for i in range(n):
        for j in range(m):
            if visit[i][j] == False and matrix[i][j] == 1:
                visit[i][j] = True
                result = dfs(i, j, 1)
                location.append(result)
    
    return(max(location))