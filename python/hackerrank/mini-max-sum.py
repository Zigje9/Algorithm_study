def miniMaxSum(arr):
    sum_number = sum(arr)
    arr.sort()
    print(sum_number-arr[-1], sum_number-arr[0])