
num_list = [3, 6, 5, 9, 1, 4, 2, 8, 7]

for i in range(1, len(num_list)):
    for j in range(i, 0, -1):
        if num_list[j-1] > num_list[j]:
            temp = num_list[j-1]
            num_list[j-1] = num_list[j]
            num_list[j] = temp
        else:
            break

print(num_list)
