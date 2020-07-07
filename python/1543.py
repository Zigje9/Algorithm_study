problem = input()
search = input()
count = 0
jump = len(search)
s_idx = 0
p_idx = len(problem)
while s_idx <= p_idx-1:
    if search == problem[s_idx:s_idx+jump]:
        count += 1
        s_idx += jump
    else:
        s_idx += 1
print(count)