import sys
import heapq

T = int(sys.stdin.readline())


def solution():
    N = int(sys.stdin.readline())
    numbers = []
    L = N // 10
    if N % 10 != 0:
        L += 1
    for _ in range(L):
        numbers += list(map(int, sys.stdin.readline().split()))
    answer = []
    left_heap = []
    right_heap = []
    heapq.heappush(left_heap, (-numbers[0], numbers[0]))
    answer.append(numbers[0])
    for i in range(1, N):
        now_mid = left_heap[0][1]
        if i % 2 == 1:
            if now_mid <= numbers[i]:
                heapq.heappush(right_heap, numbers[i])
            else:
                heapq.heappop(left_heap)
                heapq.heappush(left_heap, (-numbers[i], numbers[i]))
                heapq.heappush(right_heap, now_mid)
        else:
            right = right_heap[0]
            if right < numbers[i]:
                heapq.heappop(right_heap)
                heapq.heappush(left_heap, (-right, right))
                heapq.heappush(right_heap, numbers[i])
            else:
                heapq.heappush(left_heap, (-numbers[i], numbers[i]))
            answer.append(left_heap[0][1])

    P = len(answer)
    print(P)
    if P > 10:
        Q = P // 10
        if P % 10 != 0:
            Q += 1
        for x in range(Q):
            if x == Q-1:
                print(" ".join(map(str, answer[x*10:])))
                break
            print(" ".join(map(str, answer[x*10:x*10+10])))
    else:
        print(" ".join(map(str, answer)))


while T > 0:
    solution()
    T -= 1
