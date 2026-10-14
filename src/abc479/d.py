from atcoder.segtree import SegTree

N, Q = map(int, input().split())
L = [0] + list(map(int, input().split()))
R = list(map(int, input().split())) + [0]

INF = float("inf")
Lseg = SegTree(min, INF, L)
Rseg = SegTree(min, INF, R)

for _ in range(Q):
    s, t = map(int, input().split())
    if t < s:
        ans = min(L[s - 1], R[s - 1] + Lseg.prod(s - 1, N))
        print(ans)
    else:
        ans = min(R[s - 1], L[s - 1] + Rseg.prod(0, s))
        print(ans)
