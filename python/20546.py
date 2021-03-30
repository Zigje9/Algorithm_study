import sys

money = int(sys.stdin.readline())

stock = list(map(int, sys.stdin.readline().split()))

jun_stock = 0
jun_money = money

sung_stock = 0
sung_money = money

before_stock = 0
buy_flag = 0
sell_flag = 0

for s in stock:
    if s <= jun_money:
        jun_stock += (jun_money // s)
        jun_money -= (jun_money // s)*s

    if before_stock < s:
        sell_flag += 1
        buy_flag = 0
    elif before_stock > s:
        sell_flag = 0
        buy_flag += 1
    else:
        buy_flag = 0
        sell_flag = 0

    before_stock = s

    if buy_flag >= 3:
        if s <= sung_money:
            sung_stock += (sung_money // s)
            sung_money -= (sung_money // s)*s

    if sell_flag >= 3:
        if sung_stock > 0:
            sung_money += (sung_stock*s)
            sung_stock = 0

if jun_money+jun_stock*stock[-1] > sung_money+sung_stock*stock[-1]:
    print("BNP")
elif jun_money+jun_stock*stock[-1] < sung_money+sung_stock*stock[-1]:
    print("TIMING")
else:
    print("SAMESAME")
