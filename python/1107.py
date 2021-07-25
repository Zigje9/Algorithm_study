import sys

N = int(sys.stdin.readline())
sys.stdin.readline()
broken = list(map(int, sys.stdin.readline().split()))

answer = abs(N-100)

for i in range(1000001):
    check = list(map(int, str(i)))
    flag = True
    for n in check:
        if n in broken:
            flag = False
            break
    
    if flag == False:
        continue

    answer = min(answer, abs(N-i)+len(check))

print(answer)
