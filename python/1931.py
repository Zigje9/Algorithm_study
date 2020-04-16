import sys
N = int(sys.stdin.readline())
conferlist = []
for i in range(N):
    conferlist.append(list(map(int, sys.stdin.readline().split())))
conferlist = sorted(conferlist,reverse=True)
point = conferlist[0][0]
answer = 1
for check in conferlist:
    if check != conferlist[0]:
        if check[1] <= point:
            point = check[0]
            answer += 1

print(answer)
