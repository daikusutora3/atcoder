from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = input()
mod = 998244353


def op(a, b):
    return [
        (a[0] + b[0]) % mod,
        (a[1] + b[1]) % mod,
        (a[2] + b[2]) % mod,
        ((a[0] * b[1]) % mod + a[3] + b[3]) % mod,
        ((a[1] * b[2]) % mod + a[4] + b[4]) % mod,
        ((a[0] * b[4]) % mod + (a[3] * b[2]) % mod + a[5] + b[5]) % mod,
    ]


segtree = SegTree(
    op,
    [0, 0, 0, 0, 0, 0],
    [
        [
            A[i] if S[i] == "R" else 0,
            A[i] if S[i] == "G" else 0,
            A[i] if S[i] == "B" else 0,
            0,
            0,
            0,
        ]
        for i in range(N)
    ],
)

for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        i, x = a, b
        i -= 1
        segtree.set(
            i,
            [
                x if S[i] == "R" else 0,
                x if S[i] == "G" else 0,
                x if S[i] == "B" else 0,
                0,
                0,
                0,
            ],
        )
    else:
        l, r = a, b
        res = segtree.prod(l - 1, r)
        print(res[-1])
