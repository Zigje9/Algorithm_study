import sys
import re

S = sys.stdin.readline().rstrip()

find_S = sys.stdin.readline().rstrip()

p = re.compile("[^0-9]")
if find_S in "".join(p.findall(S)):
    print(1)
else:
    print(0)
