import sys
import heapq

N = int(sys.stdin.readline())
course = []
for _ in range(N):
    course.append(list(map(int, sys.stdin.readline().split())))

course.sort()

heap = []

heapq.heappush(heap, (course[0][1], course[0][0]))
answer = 1

for i in range(1, N):
    start, end = course[i]
    if heap[0][0] <= start:
        heapq.heappop(heap)
        heapq.heappush(heap, (end, start))
    else:
        heapq.heappush(heap, (end, start))
        answer += 1

print(answer)
