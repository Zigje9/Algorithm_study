N, M = map(str, input().split())
new_N = N[::-1]
new_M = M[::-1]
if new_N>new_M:
    print(new_N)
else:
    print(new_M)
