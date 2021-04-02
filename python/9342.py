import sys

T = int(sys.stdin.readline())


def solution():
    special = ["A", "B", "C", "D", "E", "F"]
    S = sys.stdin.readline().rstrip()
    if len(S) <= 2:
        print("Good")
        return

    if S[0] not in special:
        print("Good")
        return

    if S[-1] not in special:
        print("Good")
        return

    if S[0] != "A":
        S = S[1:]

    stage = 1
    idx = 0
    while idx < len(S):
        if stage == 1:
            if S[idx] != "A":
                print("Good")
                return
            else:
                stage = 2

        elif stage == 2:
            if S[idx] == "A":
                stage = 2
            elif S[idx] == "F":
                stage = 3
            else:
                print("Good")
                return

        elif stage == 3:
            if S[idx] == "F":
                stage = 3
            elif S[idx] == "C":
                stage = 4
            else:
                print("Good")
                return

        elif stage == 4:
            if S[idx] == "C":
                stage = 4
            else:
                stage = 5

        else:
            print("Good")
            return

        idx += 1

    print("Infected!")


while T > 0:
    solution()
    T -= 1
