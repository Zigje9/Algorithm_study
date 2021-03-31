import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == "END":
        sys.exit()
    print("".join(reversed(s)))
