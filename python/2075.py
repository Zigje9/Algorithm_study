import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    input_list = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        heapq.heappush(heap, input_list[i])
    while len(heap) > N:
        heapq.heappop(heap)

print(heap[0])
