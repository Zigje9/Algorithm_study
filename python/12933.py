import sys

sound = str(sys.stdin.readline().rstrip())

N = len(sound)

visit = [0]*N

answer = 0

for i in range(N-4):
    flag = False
    if sound[i] == "q" and visit[i] == 0:  # 출발
        j = i
        temp_duck = []
        while j <= N-1:
            if sound[j] in ["q", "u", "a", "c", "k"] and visit[j] == 0:
                if sound[j] == "q" and len(temp_duck) == 0:
                    temp_duck.append(j)
                if sound[j] == "u" and len(temp_duck) == 1:
                    temp_duck.append(j)
                if sound[j] == "a" and len(temp_duck) == 2:
                    temp_duck.append(j)
                if sound[j] == "c" and len(temp_duck) == 3:
                    temp_duck.append(j)
                if sound[j] == "k" and len(temp_duck) == 4:
                    temp_duck.append(j)
                    for k in temp_duck:
                        visit[k] = 1
                    temp_duck = []
                    flag = True
                j += 1
            else:
                j += 1
    if flag:
        answer += 1

if sum(visit) != N:
    print(-1)
else:
    print(answer)
