from atcoder.dsu import DSU

N, M = map(int, input().split())
dsu = DSU(N)
UVC = [list(map(int, input().split())) for i in range(M)]
UVC.sort(key=lambda x: x[2])
ans = 0
for u, v, c in UVC:
    u -= 1
    v -= 1
    if dsu.same(u, v):
        continue
    dsu.merge(u, v)
    ans += c
print(ans)
