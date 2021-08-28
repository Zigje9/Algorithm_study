import sys

N, M = map(int, sys.stdin.readline().split())

point = sorted(list(map(int, sys.stdin.readline().split())))

point_length = len(point)

def binarySearchLeft(k):
    left = 0
    right = point_length-1
    if k > point[point_length-1]:
        return point_length
    while left <= right:
        mid = (left + right) // 2
        if k <= point[mid]:
            if mid == 0:
                break
            if point[mid-1] < k:
                break
            right = mid - 1
        else:
            left = mid + 1
    return mid

def binarySearchRight(k):
    left = 0
    right = point_length-1
    if k < point[0]:
        return -1
    while left <= right:
        mid = (left + right) // 2
        if point[mid] <= k:
            if mid == point_length-1:
                break
            if k < point[mid+1]:
                break
            left = mid + 1
        else:
            right = mid -1
    return mid

        

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(binarySearchRight(e) - binarySearchLeft(s) + 1)