import sys

K, N = map(int, sys.stdin.readline().split())

lan_list = []
for i in range(K):
    lan_list.append(int(input()))

lan_list.sort()

global answer


def binary_search(left, right):
    while left <= right:
        mid = (left+right)//2
        count = 0
        for lan in lan_list:
            count += (lan // mid)
        if count >= N:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


def solution():
    print(binary_search(1, lan_list[-1]))


solution()
