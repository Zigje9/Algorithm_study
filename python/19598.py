import sys
import heapq

N = int(sys.stdin.readline())

meeting = []

for _ in range(N):
    meeting.append(list(map(int, sys.stdin.readline().split())))

meeting.sort(key=lambda x: x[0])
answer = 1
room = []

for start, end in meeting:
    if len(room) == 0:
        heapq.heappush(room, end)
        continue
    
    while room:
        if room[0] > start:
            heapq.heappush(room, end)
            answer = max(answer, len(room))
            break
        else:
            heapq.heappop(room)
    
print(answer)

