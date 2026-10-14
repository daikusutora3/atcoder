from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))
sl = SortedList(A)
now = 0
ans = 0
while len(sl) > 0:
    bl = sl.bisect_left(now)
    if len(sl) == bl or (bl > 0 and abs(now - sl[bl - 1]) <= abs(now - sl[bl])):
        bl -= 1
    ans += abs(now - sl[bl])
    now = sl[bl]
    sl.discard(now)
    # print(now, sl, ans)

print(ans)
