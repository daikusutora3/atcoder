from collections import defaultdict

from sortedcontainers import SortedList


N, Q = map(int, input().split())
sl = SortedList([0 for i in range(N)])
d = defaultdict(int)

cnt = 0
ans = []
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, x = map(int, query.split())
        sl.remove(d[x])
        d[x] += 1
        sl.add(d[x])
        if sl[0] == cnt + 1:
            cnt += 1
    elif query[0] == "2":
        _, y = map(int, query.split())
        bl = sl.bisect_left(y + cnt)
        ans.append(N - bl)

print(*ans, sep="\n")
