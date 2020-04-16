import sys
N, Money = map(int, (sys.stdin.readline().split()))
coin = []
answer = 0

for i in range(N):
    coin.append(int(sys.stdin.readline()))

while Money > 0:
    if Money >= coin[N-1]:
        answer += int(Money/coin[N-1])
        Money -= int(Money/coin[N-1])*coin[N-1]
    N -= 1

print(answer)