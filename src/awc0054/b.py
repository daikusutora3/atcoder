from heapq import heappop, heappush


N, W = map(int, input().split())

lw = [list(map(int, input().split())) for i in range(N)]
lw.sort()

pq = []

ans = 0
now = 0
for i in range(N):
    l, w = lw[i]
    while len(pq) and pq[0] <= l:
        ans += abs(now - pq[0])
        now = heappop(pq)

    if len(pq) > 0:
        ans += l - now
    now = l
    heappush(pq, l + w)

while len(pq) and pq[0] <= float("inf"):
    ans += abs(now - pq[0])
    now = heappop(pq)

print(ans)
