from atcoder.dsu import DSU

N, M = map(int, input().split())
dsu = DSU(N)

d = dict()

for i in range(N):
    d[i] = -1

for _ in range(M):
    U, V, C = map(int, input().split())
    dsu.merge(U - 1, V - 1)
    d[dsu.leader(U - 1)] = C

ans = set()
for i in range(N):
    ans.add(d[dsu.leader(i)])

print(len(ans - {-1}))
