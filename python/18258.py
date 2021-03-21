import sys
from collections import deque

q = deque()

N = int(sys.stdin.readline())


def push(X):
    q.append(X)


def pop():
    if len(q) == 0:
        print(-1)
    else:
        print(q.popleft())


def size():
    print(len(q))


def empty():
    if len(q) == 0:
        print(1)
    else:
        print(0)


def front():
    if len(q) == 0:
        print(-1)
    else:
        print(q[0])


def back():
    if len(q) == 0:
        print(-1)
    else:
        print(q[-1])


for _ in range(N):
    command = list(sys.stdin.readline().split())
    c = command[0]
    if c == "push":
        push(command[1])
        continue
    if c == "pop":
        pop()
        continue
    if c == "size":
        size()
        continue
    if c == "empty":
        empty()
        continue
    if c == "front":
        front()
        continue
    if c == "back":
        back()
        continue
