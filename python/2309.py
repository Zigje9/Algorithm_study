import sys
people = []
total = 0
for i in range(9):
    N = int(sys.stdin.readline())
    people.append(N)
    total += N
people.sort()
normal = total - 100


def print_dwarf(i, j):
    for k in range(9):
        if k == i or k == j:
            continue
        print(people[k])


for i in range(9):
    for j in range(9):
        if i != j:
            if people[i]+people[j] == normal:
                print_dwarf(i, j)
                normal = 1000
                break
