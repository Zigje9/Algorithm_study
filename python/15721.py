import sys

A = int(sys.stdin.readline())
T = int(sys.stdin.readline())
V = int(sys.stdin.readline())


p = 2
N = 0
while True:
    for i in range(4):
        N += 1
        if i % 2 == V:
            T -= 1
            if T == 0:
                if N < A:
                    print(N-1)
                else:
                    if N % A == 0:
                        print(A-1)
                    else:
                        print(N % A-1)
                sys.exit()
    for j in range(p):
        N += 1
        if V == 0:
            T -= 1
            if T == 0:
                if N < A:
                    print(N-1)
                else:
                    if N % A == 0:
                        print(A-1)
                    else:
                        print(N % A-1)
                sys.exit()

    for k in range(p):
        N += 1
        if V == 1:
            T -= 1
            if T == 0:
                if N < A:
                    print(N-1)
                else:
                    if N % A == 0:
                        print(A-1)
                    else:
                        print(N % A-1)
                sys.exit()
    p += 1
