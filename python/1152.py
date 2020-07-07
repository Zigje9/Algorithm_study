S = input()
count = 1
for i in S:
    if i == ' ':
        count += 1
if S[0] == ' ':
    count -= 1
if S[-1] == ' ':
    count -= 1
print(count)