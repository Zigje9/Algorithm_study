import sys

N, K = map(int, sys.stdin.readline().split())

check = str(K)

answer = 0
for i in range(N*3600+59*60+59+1):
    temp = ""
    if len(str(i//3600)) == 1:
        temp += "0"
    temp += str(i//3600)
    if len(str(i % 3600//60)) == 1:
        temp += "0"
    temp += str(i % 3600//60)
    if len(str(i % 3600 % 60)) == 1:
        temp += "0"
    temp += str(i % 3600 % 60)
    if check in temp:
        answer += 1

print(answer)
