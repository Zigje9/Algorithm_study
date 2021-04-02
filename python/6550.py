import sys


def solution(s, t):
    if len(s) > len(t):
        print("No")
        return

    right = 0
    for char in s:
        if right == len(t):
            print("No")
            return
        while right < len(t):
            if char == t[right]:
                right += 1
                break
            else:
                if len(t)-1 == right:
                    print("No")
                    return
                right += 1

    print("Yes")


while True:
    try:
        s, t = map(str, sys.stdin.readline().rstrip().split())
        solution(s, t)
    except:
        break
