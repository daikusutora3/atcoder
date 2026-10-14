from atcoder.segtree import SegTree

N, C, Q = map(int, input().split())
A = list(map(int, input().split()))


def op(a, b):
    res = [[0 for h in range(C + 1)], [0 for h in range(C + 1)]]
    for h in range(C + 1):
        res[0][h] = b[0][a[0][h]]
        res[1][h] = b[1][a[0][h]] + a[1][h]

    return res


segtree = SegTree(
    op,
    [[h for h in range(C + 1)], [0 for h in range(C + 1)]],
    [
        [
            [h - A[i] if h >= A[i] else h for h in range(C + 1)],
            [1 if h >= A[i] else 0 for h in range(C + 1)],
        ]
        for i in range(N)
    ],
)


for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, p, x = map(int, query.split())
        segtree.set(
            p - 1,
            [
                [h - x if h >= x else h for h in range(C + 1)],
                [1 if h >= x else 0 for h in range(C + 1)],
            ],
        )
    else:
        _, l, r, d = map(int, query.split())
        print(segtree.prod(l - 1, r)[1][d])
