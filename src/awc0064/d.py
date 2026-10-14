from atcoder.dsu import DSU

N, M = map(int, input().split())
UVC = [list(map(int, input().split())) for i in range(M)]

UVC.sort(key=lambda x: x[2])
dsu = DSU(N)
ans = 0
for u, v, c in UVC:
    u, v = u - 1, v - 1
    if not dsu.same(u, v):
        dsu.merge(u, v)
        ans += c

print(ans if len(dsu.groups()) == 1 else -1)
