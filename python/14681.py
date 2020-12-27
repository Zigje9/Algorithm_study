import sys

X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())

if X>0 and Y>0:
  print(1)

if X>0 and Y<0:
  print(4)

if X<0 and Y>0:
  print(2)

if X<0 and Y<0:
  print(3)