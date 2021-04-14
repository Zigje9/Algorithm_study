parent = [0, 1, 2, 3, 4, 5, 6, 7]  # 인덱스와 노드의 번호가 일치하도록

graph = [[1, 2], [1, 3], [4, 6], [5, 6], [6, 7]]  # 간선 정보
# 부모노드를 찾는 재귀 함수


def get_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    return False


# 그래프를 돌면서 간선을 이어주고 parent 배열을 갱신한다.
for x, y in graph:
    union_parent(parent, x, y)

print(parent)
