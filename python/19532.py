import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

print((e*c-b*f)//(e*a-b*d), (d*c-a*f)//(b*d-a*e))
