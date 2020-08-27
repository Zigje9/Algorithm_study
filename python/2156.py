t = int(input())

grapes = [0]
DP = [0]*10001

for i in range(t):
    grape = int(input())
    grapes.append(grape)


def drink():
    DP[0] = grapes[0]
    DP[1] = grapes[1]
    DP[2] = grapes[2] + grapes[1]
    DP[3] = max(grapes[2] + grapes[3], grapes[1] + grapes[3], grapes[1] + grapes[2])

    for idx in range(4, t+1):
        DP[idx] = max(DP[idx-1], DP[idx-2] + grapes[idx], DP[idx-3] + grapes[idx-1] + grapes[idx])

    print(max(DP))


if t == 1:
    print(grapes[1])

elif t == 2:
    print(grapes[1]+grapes[2])

else:
    drink()