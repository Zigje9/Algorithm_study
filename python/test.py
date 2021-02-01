# A = [[0]*3]*3

# print(A)

# A[0][1] = 1

# print(A)

# B = [[0]*3 for i in range(3)]

# print(B)

# B[0][1] = 1

# print(B)

# a = "123"
# b = "1234"


# print(True and True)print(a.startswith(b))
# print(b.startswith(a))
# print(a in b)
# print(b in a)
# print("----")
# print(True and False)
# print(False and True)
# print(False and False)

def dfs(i, j):
    print(i, j)
    if j==2:
        i += 1
        j = i + 1
    else:
        j += 1
    if i == 2:
        return
    dfs(i, j)
    dfs(i, j)
    dfs(i, j)

dfs(0, 1)
