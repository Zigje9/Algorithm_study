import sys

N = int(sys.stdin.readline().rstrip())
marble = list(map(int, sys.stdin.readline().split()))
answer = []


def dfs(marble, visit, val, count):
    if count == 0:
        answer.append(val)
        return
    for i in range(1, len(visit)-1):
        if visit[i] == 0:
            visit[i] = 1
            left = i-1
            right = i+1
            while True:
                if visit[left] == 0:
                    break
                left -= 1
            while True:
                if visit[right] == 0:
                    break
                right += 1
            dfs(marble, visit, val+marble[left]*marble[right], count-1)
            visit[i] = 0
    return


def solution():
    visit = []
    for _ in range(len(marble)):
        visit.append(0)
    dfs(marble, visit, 0, len(marble)-2)
    print(max(answer))


solution()
