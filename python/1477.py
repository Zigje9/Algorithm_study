import sys

N, M, L = map(int, sys.stdin.readline().split())

rest = list(map(int, sys.stdin.readline().split()))

rest.append(0)
rest.append(L)
rest.sort()

left = 0
right = L
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in range(N+1):
        if (rest[i+1]-rest[i]) > mid:
            count += (rest[i+1]-rest[i]-1) // mid
    if count > M:
        left = mid + 1
    elif count <= M:
        answer = mid
        right = mid - 1


print(answer)



