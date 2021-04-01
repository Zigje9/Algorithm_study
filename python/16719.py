import sys
from itertools import combinations

ZOAC = list(map(str, sys.stdin.readline().rstrip()))

check = [0]*len(ZOAC)


def print_c():
    p = ""
    for i in range(len(check)):
        if check[i] == 1:
            p += ZOAC[i]
    print(p)


for _ in range(len(ZOAC)):
    idx = len(ZOAC)-1
    temp = "?"
    temp_idx = 0
    flag = True
    while idx >= 0:
        if check[idx] == 1:
            if temp != "?":
                flag = False
                check[temp_idx] = 1
                print_c()
                break
            else:
                idx -= 1
        else:
            if temp == "?":
                temp = ZOAC[idx]
                temp_idx = idx
                idx -= 1
            else:
                if temp >= ZOAC[idx]:
                    temp = ZOAC[idx]
                    temp_idx = idx
                    idx -= 1
                else:
                    idx -= 1
    if flag == True:
        check[temp_idx] = 1
        print_c()
