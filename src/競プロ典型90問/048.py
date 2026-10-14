from heapq import heappop, heappush


N, K = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

# 0: 何にも解いていない, 1: 部分問題だけ解いている 2: 満点
d = [0 for i in range(N)]

pq = []

for i in range(N):
    heappush(pq, (-AB[i][1], i))

ans = 0
while pq and K:
    tokuten, id = heappop(pq)
    ans -= tokuten
    K -= 1
    if d[id] == 0:
        d[id] = 1
        heappush(pq, (-(AB[id][0] - AB[id][1]), id))

print(ans)
