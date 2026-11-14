from sortedcontainers import SortedList

N, L, R = map(int, input().split())

A = list(map(int, input().split()))
rui = [0 for i in range(N + 1)]
for i in range(N):
    rui[i + 1] += rui[i] + A[i]

sl = SortedList()

ans = 0
for r in range(N):
    sl.add(rui[r])
    ll = sl.bisect_left(rui[r + 1] - R)
    lr = sl.bisect_right(rui[r + 1] - L)
    ans += lr - ll

print(ans)
