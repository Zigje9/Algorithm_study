import sys

N = int(sys.stdin.readline().rstrip())
length = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()


def solution():
    answer = 0
    i = 0
    while i <= length-3:
        if S[i] == "I":
            check = 0
            while S[i+1]+S[i+2] == "OI":
                check += 1
                if check == N:
                    answer += 1
                    check -= 1
                if(i+2 <= length-3):
                    i += 2
                else:
                    break
            i += 1
        else:
            i += 1
    print(answer)


solution()
