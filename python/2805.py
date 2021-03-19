import sys

N, M = map(int, sys.stdin.readline().split())

tree = sorted(list(map(int, sys.stdin.readline().split())))


def getTree(H):
    height = 0
    for t in tree:
        if t <= H:
            continue
        height += (t-H)
    return height


left = 0
right = tree[-1]

while left <= right:
    mid = (left + right) // 2
    if getTree(mid) >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)
