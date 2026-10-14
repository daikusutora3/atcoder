from heapq import heappop, heappush

from atcoder.dsu import DSU

N = int(input())
uf = DSU(N)
hq = []

ixy = []

for i in range(N):
    x, y = map(int, input().split())
    ixy.append((i, x, y))

# xに関してソートして辺を考える
ixy.sort(key=lambda x: x[1])
for i in range(N - 1):
    v, vx, vy = ixy[i]
    nv, nvx, nvy = ixy[i + 1]
    heappush(hq, (abs(vx - nvx), v, nv))

# yに関してソートして辺を考える
ixy.sort(key=lambda x: x[2])
for i in range(N - 1):
    v, vx, vy = ixy[i]
    nv, nvx, nvy = ixy[i + 1]
    heappush(hq, (abs(vy - nvy), v, nv))

ans = 0
while len(hq):
    cost, u, v = heappop(hq)
    if uf.leader(u) == uf.leader(v):
        continue
    uf.merge(u, v)
    ans += cost

print(ans)
