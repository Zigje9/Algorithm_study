def hansoo(list,M):
    N = M + 1
    if N < 100:
        list[N-1] = 1
    else:
        if (int(N/100) - int(N/10%10)) == (int(N/10%10) - int(N%10)):
            list[N-1] = 1


N = int(input())
hanlist = []
sum = 0
for i in range(0,N):
    hanlist.append(0)
for j in range(0,N):
    hansoo(hanlist,j)
for k in range(0,N):
    if hanlist[k] == 1:
        sum += 1
print(sum)

