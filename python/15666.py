import sys
N, M = map(int, sys.stdin.readline().split())

num_list = sorted(list(map(int, sys.stdin.readline().split())))


def bfs(start, answer):
    if start == M:
        print(' '.join(map(str, answer)))
        return
    check = -1
    for idx in range(N):
        if check != num_list[idx]:
            if len(answer) == 0:
                answer.append(num_list[idx])
                check = num_list[idx]
                bfs(start+1, answer)
                answer.pop(-1)
            else:
                if answer[-1] <= num_list[idx]:
                    answer.append(num_list[idx])
                    check = num_list[idx]
                    bfs(start+1, answer)
                    answer.pop(-1)


bfs(0, [])
