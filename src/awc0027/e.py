from sortedcontainers import SortedList


N, M, K = map(int, input().split())
A = list(map(int, input().split()))

A = [a + M for a in A]
rui = [0 for i in range(N + 1)]
for i in range(N):
    rui[i + 1] = rui[i] + A[i]

ans = 0
sl = SortedList()
for r in range(N + 1):
    bl = sl.bisect_left(rui[r] - K)
    ans += len(sl) - bl
    sl.add(rui[r])

print(ans)
