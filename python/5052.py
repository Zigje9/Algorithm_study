import sys
T = int(sys.stdin.readline())
answer = []

def checker(answer, book, num):
    for i in range(num-1):
        if book[i].startswith(book[i+1]) or book[i+1].startswith(book[i]): 
            answer.append("NO")
            return
    answer.append("YES")
    return

while T > 0:
    N = int(sys.stdin.readline())
    phone_book = []
    for i in range(N):
        phone_book.append(sys.stdin.readline().strip())
    phone_book.sort()
    checker(answer, phone_book, N)
    T -= 1

for i in answer:
    print(i)