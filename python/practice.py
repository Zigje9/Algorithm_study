A = [11, 12, 13, 14, 15, 16, 17, 18, 19, 110]
target = 13
al = len(A)
left = 0
right = al-1
while left <= right:
    mid = (left+right)//2
    if A[mid] == target:
        print(mid+1)
        break
    elif A[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
