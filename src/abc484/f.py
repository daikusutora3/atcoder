from atcoder.segtree import SegTree

INF = float("inf")


def op(a, b):
    if a == b:
        return a
    elif a == -1:
        return b
    elif b == -1:
        return a
    else:
        return INF


N, Q = map(int, input().split())
A = list(map(int, input().split()))

segtree = SegTree(op, -1, A)
for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        i, x = a, b
        segtree.set(i - 1, x)
    else:
        l, r = a, b
        ans = segtree.prod(l - 1, r)
        if ans == INF:
            print("No")
        else:
            print("Yes")
