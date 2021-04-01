import sys

sero = []
max_len = 1
for _ in range(5):
    temp = sys.stdin.readline().rstrip()
    length_temp = len(temp)
    if length_temp < 15:
        temp += "!"*(15-length_temp)
    sero.append(temp)
    if length_temp > max_len:
        max_len = length_temp

answer = ""

for i in range(max_len):
    for j in range(5):
        if sero[j][i] != "!":
            answer += sero[j][i]

print(answer)
