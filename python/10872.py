N = int(input())
Sum = 1
if N == 0:
    print(1)
else:
    while N>0:
        Sum *= N
        N -= 1
    print(Sum)