from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

INF = float("inf")
segtree = SegTree(min, INF, A)


for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        i, x = a, b
        segtree.set(i - 1, x)
    else:
        l, r = a, b
        res = segtree.prod(l - 1, r)
        print(res)
