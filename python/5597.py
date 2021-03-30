import sys

students = []
for _ in range(28):
    students.append(int(sys.stdin.readline()))

for i in range(1, 31):
    if i not in students:
        print(i)
