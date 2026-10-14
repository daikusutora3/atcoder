from sortedcontainers import SortedList


X = int(input())
Q = int(input())

sl = SortedList([X])


for _ in range(Q):
    A, B = map(int, input().split())
    sl.add(A)
    sl.add(B)
    print(sl[len(sl) // 2])
