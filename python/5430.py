import sys

T = int(sys.stdin.readline())

def solution():
    command = list(sys.stdin.readline().rstrip())
    ll = int(sys.stdin.readline())
    if ll == 0:
        sys.stdin.readline()
        if 'D' in command:
            print('error')
            return
        print("[]")
        return
    arr = list(map(int, sys.stdin.readline()[1:-2].split(',')))
    left = 0
    right = ll-1
    turn = True
    for c in command:
        if c == 'R':
            if turn:
                turn = False
            else:
                turn = True
        else:
            if turn:
                left += 1
            else:
                right -= 1
            if left > right + 1:
                print('error')
                return
    if left == right+1:
        print("[]")
        return
    if turn:
        print(str(arr[left:right+1]).replace(" ",""))
    else:
        print(str(arr[left:right+1][::-1]).replace(" ",""))

while T > 0:
    solution()
    T -= 1