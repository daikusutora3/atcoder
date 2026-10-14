from sortedcontainers import SortedList


Q = int(input())
sl = SortedList()
for _ in range(Q):
    q, h = map(int, input().split())
    if q == 1:
        sl.add(h)
    else:
        while len(sl) and sl[0] <= h:
            sl.discard(sl[0])
    print(len(sl))
