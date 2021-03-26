import sys

poly = str(sys.stdin.readline().rstrip())

count = 0
answer = ""
flag = True
for p in poly:
    if p == "X":
        count += 1
    else:
        if count == 0:
            answer += "."
        else:
            if count % 2 != 0:
                print(-1)
                sys.exit()
            answer += ((count // 4) * "AAAA" + (count % 4) * "B")
            answer += "."
            count = 0
if count != 0:
    if count % 2 != 0:
        print(-1)
        sys.exit()
    answer += ((count // 4) * "AAAA" + (count % 4) * "B")

print(answer)
