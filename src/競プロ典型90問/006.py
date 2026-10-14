import heapq

N, K = map(int, input().split())
S = input()

pq = []
for i in range(N - K):
    heapq.heappush(pq, [S[i], i])

# [[char, index], ...]
ans = [["&", -1]]
for i in range(N - K, N):
    heapq.heappush(pq, [S[i], i])
    s, j = heapq.heappop(pq)
    while ans[-1][1] >= j:
        s, j = heapq.heappop(pq)
    ans.append([s, j])

print(*[ans[i][0] for i in range(1, K + 1)], sep="")
