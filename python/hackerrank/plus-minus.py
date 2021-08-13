def plusMinus(arr):
    n = len(arr)
    positive = 0
    negative = 0
    zeros = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zeros += 1
    
    print(positive / n)
    print(negative / n)
    print(zeros / n)