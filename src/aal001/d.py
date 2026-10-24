from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))


def op(a, b):
    cnt0 = a[0] + b[0]
    cnt1 = a[1] + b[1]
    cnt2 = a[2] + b[2]
    tentou = a[3] + b[3] + a[2] * (b[0] + b[1]) + a[1] * b[0]
    return [cnt0, cnt1, cnt2, tentou]


segtree = SegTree(
    op,
    [0, 0, 0, 0],
    [[1 if a == 0 else 0, 1 if a == 1 else 0, 1 if a == 2 else 0, 0] for a in A],
)

for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        i, x = a, b
        segtree.set(
            i - 1, [1 if x == 0 else 0, 1 if x == 1 else 0, 1 if x == 2 else 0, 0]
        )
    else:
        l, r = a, b
        res = segtree.prod(l - 1, r)
        print(res[3])
