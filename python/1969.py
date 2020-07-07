N, M = map(int, input().split())
D = ['A', 'C', 'G', 'T']
D_count = [0, 0, 0, 0]
DNA = []
answer = []
ans_sum = 0
for i in range(N):
    DNA.append(input())

for i in range(M):
    for j in range(N):
        if DNA[j][i] == 'A':
            D_count[0] += 1
        elif DNA[j][i] == 'C':
            D_count[1] += 1
        elif DNA[j][i] == 'G':
            D_count[2] += 1
        else:
            D_count[3] += 1

    answer.append(D[D_count.index(max(D_count))])
    ans_sum += sum(D_count)-D_count[D_count.index(max(D_count))]
    D_count = [0, 0, 0, 0]
print(''.join(answer))
print(ans_sum)