from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))


def op(x, y):
    return x + y


segtree = SegTree(op, 0, A)

for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        i, x = a, b
        segtree.set(i - 1, x)
    elif q == 2:
        l, t = a, b
        mr = segtree.max_right(l - 1, lambda x: x < t)  # noqa: B023
        print(mr + 1)
    else:
        r, t = a, b
        ml = segtree.min_left(r, lambda x: x < t)  # noqa: B023
        print(ml)
