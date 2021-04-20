import sys
import heapq

INF = sys.maxsize

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

T = 1


def solution(N, T):
    board = []
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))

    score = [[INF]*N for _ in range(N)]

    def bfs(x, y):
        heap = []
        heapq.heappush(heap, [board[x][y], x, y])
        score[x][y] = board[x][y]
        while heap:
            now_value, now_x, now_y = heapq.heappop(heap)
            for i in range(4):
                next_x = now_x + move_x[i]
                next_y = now_y + move_y[i]
                if 0 <= next_x < N and 0 <= next_y < N:
                    if now_value + board[next_x][next_y] < score[next_x][next_y]:
                        score[next_x][next_y] = now_value + \
                            board[next_x][next_y]
                        heapq.heappush(
                            heap, [score[next_x][next_y], next_x, next_y])

    bfs(0, 0)
    print("Problem %d: %d" % (T, score[N-1][N-1]))


while True:
    num = int(sys.stdin.readline())
    if num == 0:
        sys.exit()
    solution(num, T)
    T += 1
