def diagonalDifference(arr):
    n = len(arr)
    answer = 0 
    for i in range(n):
        answer += (arr[i][i] - arr[i][n-1-i])
    return abs(answer)