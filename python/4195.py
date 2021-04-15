import sys

T = int(sys.stdin.readline())


def solution():

    def get_parent(parent, S):
        if parent[S] == S:
            return S
        parent[S] = get_parent(parent, parent[S])
        return parent[S]

    def union_parent(parent, a, b):
        a = get_parent(parent, a)
        b = get_parent(parent, b)
        if a != b:
            parent[b] = a
            friend_network[a] += friend_network[b]
            friend_network[b] = 0

    friend = {}
    friend_network = {}
    N = int(sys.stdin.readline())
    for _ in range(N):
        A, B = sorted(list(map(str, sys.stdin.readline().split())))
        if A not in friend:
            friend[A] = A
            friend_network[A] = 1
        if B not in friend:
            friend[B] = B
            friend_network[B] = 1
        union_parent(friend, A, B)

        print(friend_network[get_parent(friend, A)])


while T > 0:
    solution()
    T -= 1
