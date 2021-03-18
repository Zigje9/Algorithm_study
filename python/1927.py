import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if len(heap) == 0:
            print(0)
            continue
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, command)
