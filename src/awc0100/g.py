from atcoder.dsu import DSU

N, M = map(int, input().split())
dsu = DSU(N)
for _ in range(M):
    u, v = map(int, input().split())
    dsu.merge(u - 1, v - 1)

Q = int(input())
for _ in range(Q):
    S = int(input())
    print(dsu.size(S - 1))
