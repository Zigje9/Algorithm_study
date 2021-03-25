import sys
import heapq

T = int(sys.stdin.readline())


def solution():
    N = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    ids = [0] * 1000001
    for i in range(N):
        command, num = map(str, sys.stdin.readline().split())
        if command == "I":
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
            ids[i] = 1
        else:
            if int(num) == 1:
                while len(max_heap) > 0 and ids[max_heap[0][1]] == 0:
                    heapq.heappop(max_heap)
                if len(max_heap) > 0:
                    ids[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)

            else:
                while len(min_heap) > 0 and ids[min_heap[0][1]] == 0:
                    heapq.heappop(min_heap)
                if len(min_heap) > 0:
                    ids[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    while len(max_heap) > 0 and ids[max_heap[0][1]] == 0:
        heapq.heappop(max_heap)
    while len(min_heap) > 0 and ids[min_heap[0][1]] == 0:
        heapq.heappop(min_heap)

    if len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])


while T > 0:
    solution()
    T -= 1
