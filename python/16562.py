import sys

N, M, k = map(int, sys.stdin.readline().split())

friend = []
friend_money = [0]
for i in range(N+1):
    friend.append(i)

friend_money += list(map(int, sys.stdin.readline().split()))


def get_parent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent, parent[x])
        change_friend_money(friend_money, x, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def change_friend_money(friend_money, a, b):
    if friend_money[a] > friend_money[b]:
        friend_money[a] = friend_money[b]
    else:
        friend_money[b] = friend_money[a]


for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    union_parent(friend, A, B)
    change_friend_money(friend_money, A, B)

for i in range(1, N+1):
    get_parent(friend, i)

friend_list = {}
money = 0
for i in range(1, N+1):
    if friend[i] in friend_list:
        continue
    else:
        money += friend_money[i]
        if k < money:
            print("Oh no")
            sys.exit()
        friend_list[friend[i]] = True

print(money)
