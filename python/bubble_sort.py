num_list = [3, 6, 5, 9, 1, 4, 2, 8, 7]

for i in range(0, len(num_list)-1):
    for j in range(0, len(num_list)-1-i):
        if num_list[j] > num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp

print(num_list)
