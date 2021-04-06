import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    A, B, V = map(int, sys.stdin.readline().split())
    graph[A].append([B, V])
    graph[B].append([A, V])


first_node = []
second_node = []


def dfs(start, dist, visit, flag):
    is_next = False

    for node, value in graph[start]:
        if visit[node] == 0:
            is_next = True
            visit[node] = 1
            dfs(node, dist+value, visit, flag)
            visit[node] = 0

    if is_next == False:
        if flag == 1:
            first_node.append([start, dist])
        else:
            second_node.append([start, dist])


v = [0]*(N+1)
v[1] = 1
dfs(1, 0, v, 1)
s = sorted(first_node, key=lambda x: -x[1])

vi = [0]*(N+1)
vi[s[0][0]] = 1
dfs(s[0][0], 0, vi, 2)
ans = sorted(second_node, key=lambda x: -x[1])
print(ans[0][1])
