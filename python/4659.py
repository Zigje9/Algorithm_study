import sys

aeiou = ["a", "e", "i", "o", "u"]


def check1(password):
    for p in password:
        if p in aeiou:
            return True
    return False


def check2(password):
    left = 0
    right = 0
    for p in password:
        if p in aeiou:
            right += 1
            left = 0
            if right >= 3:
                return False
        else:
            right = 0
            left += 1
            if left >= 3:
                return False
    return True


def check3(password):
    now_word = "?"
    for p in password:
        if p == now_word:
            if p == "e" or p == "o":
                continue
            else:
                return False
        else:
            now_word = p
    return True


while True:
    S = sys.stdin.readline().rstrip()
    if S == "end":
        break

    if check1(S) and check2(S) and check3(S):
        print("<"+S+">", "is acceptable.")
    else:
        print("<"+S+">", "is not acceptable.")
