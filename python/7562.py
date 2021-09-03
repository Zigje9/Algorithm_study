import sys
from collections import deque

move_x = [-2,-1,1,2,2,1,-1,-2]
move_y = [1,2,2,1,-1,-2,-2,-1]

def solution():
    I = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())

    visit = [[False] * I for _ in range(I)]

    def bfs():
        q = deque()
        q.append([start_x, start_y, 0])
        visit[start_x][start_y] = True
        while q:
            [now_x, now_y, now_count] = q.popleft()
            if now_x == end_x and now_y == end_y:
                return now_count

            for i in range(8):
                next_x = now_x+move_x[i]
                next_y = now_y+move_y[i]
                if 0 <= next_x < I and 0 <= next_y < I:
                    if visit[next_x][next_y] == False:
                        visit[next_x][next_y] = True
                        q.append([next_x, next_y, now_count+1])
    return bfs()

T = int(sys.stdin.readline())

while T > 0:
    print(solution())
    T -= 1