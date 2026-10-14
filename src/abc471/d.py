from sortedcontainers import SortedList

Q, V = map(int, input().split())
sl = SortedList()

for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, t, w = map(int, query.split())
        sl.add(w - t)
    else:
        _, t = map(int, query.split())
        if len(sl) == 0:
            print(-1)
            continue
        print(min(V, sl[-1] + t))
        sl.discard(sl[-1])
