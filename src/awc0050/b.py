from heapq import heappop, heappush


N, K = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]
AB.sort(key=lambda x: -x[1])

pq = []
ans = 0
for i in range(N):
    while len(pq) and -pq[0] >= AB[i][1] and K > 0:
        ans += -heappop(pq)
        K -= 1
    ans += AB[i][1] * min(K, (AB[i][0] // AB[i][1]))
    K -= min(K, (AB[i][0] // AB[i][1]))
    heappush(pq, -(AB[i][0] % AB[i][1]))

while K and len(pq):
    ans += -heappop(pq)
    K -= 1

print(ans)
