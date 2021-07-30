import sys

L = int(sys.stdin.readline())

inorder = list(map(int, sys.stdin.readline().split()))

answer = [[] for _ in range(L)]

def get_tree(level, nums):
    if level == L-1:
        answer[level].append(nums[0])
        return
    
    N = len(nums)
    center = N // 2
    answer[level].append(nums[center])
    get_tree(level+1, nums[:center])
    get_tree(level+1, nums[center+1:])

get_tree(0, inorder)

for arr in answer:
    print(" ".join(map(str, arr)))