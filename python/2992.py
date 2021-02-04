import sys
N = int(sys.stdin.readline())
numList = list(map(str, str(N)))
answer = []


def dfs(visit, count, temp):
    if temp:
        if temp[0] == 0:
            return
    if count == 0:
        if int(temp) > N:
            answer.append(int(temp))
        return
    for i in range(len(numList)):
        if visit[i] == 0:
            visit[i] = 1
            temp += numList[i]
            dfs(visit, count-1, temp)
            visit[i] = 0
            temp = temp[0:len(temp)-1]


dfs([0]*len(numList), len(numList), "")
if len(answer) == 0:
    print(0)
else:
    print(sorted(answer)[0])
