import sys

forest = {}
count = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if tree:
        count += 1
        if tree in forest:
            forest[tree] += 1
        else:
            forest[tree] = 1
    else:
        break

for tree in sorted(forest):
    print(tree, '%.4f' % (forest[tree]/count*100))
