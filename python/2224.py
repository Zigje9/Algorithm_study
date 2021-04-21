import sys

N = int(sys.stdin.readline())

graph = {}

proposition = {}

for _ in range(N):
    S = sys.stdin.readline().rstrip()
    proposition[S[0]] = True
    proposition[S[-1]] = True
    if S[0] in graph:
        graph[S[0]][S[-1]] = True
    else:
        graph[S[0]] = {}
        graph[S[0]][S[-1]] = True

key_list = list(proposition.keys())
L = len(key_list)

pro = [[False]*L for _ in range(L)]

for i in range(L):
    for j in range(L):
        if key_list[i] in graph:
            if key_list[j] in graph[key_list[i]]:
                pro[i][j] = True

for k in range(L):
    for i in range(L):
        for j in range(L):
            if pro[i][k] and pro[k][j]:
                pro[i][j] = True

answer = []
for i in range(L):
    for j in range(L):
        if i == j:
            continue
        if pro[i][j]:
            answer.append([key_list[i], key_list[j]])

answer.sort(key=lambda x: (x[0], x[1]))

print(len(answer))

for p in answer:
    print(p[0], "=>", p[1])
