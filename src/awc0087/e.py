from atcoder.segtree import SegTree

N, Q = map(int, input().split())
X = []

for _ in range(N):
    S, P = input().split()
    X.append(int(P) * (1 if S == "T" else -1))


def op(a, b):
    s = a[0] + b[0]
    pb = min(a[1], a[0] + b[1])
    sb = min(b[2], b[0] + a[2])
    best = min(*[a[3], b[3], a[2] + b[1]])
    aokis = a[4] + b[4]
    return [s, pb, sb, best, aokis]


# [a, pb, sb, best, aokis]
segtree = SegTree(
    op,
    [0, float("inf"), float("inf"), float("inf"), 0],
    [[x, min(0, x), min(0, x), min(0, x), min(0, x)] for x in X],
)


for _ in range(Q):
    L, R = map(int, input().split())
    s, pb, sb, best, aokis = segtree.prod(L - 1, R)
    print(-aokis + best)
