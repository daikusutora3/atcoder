from atcoder.lazysegtree import LazySegTree

mod = 998244353


id_ = (1, 0)
e = (0, 0)


# valueの型: (sum, len)
def op(x, y):
    return ((x[0] + y[0]) % mod, x[1] + y[1])


# 上のブロックの作用素を下のブロックの値に伝播
# f = (b, c)
def mapping(f, x):
    b, c = f
    return ((b * x[0] + c * x[1]) % mod, x[1])


# 上のブロックの作用素を下のブロックの作用素に伝播
def composition(f, g):
    b, c = f
    bg, cg = g
    return ((bg * b) % mod, (cg * b + c) % mod)


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = [(a, 1) for a in A]
segtree = LazySegTree(op, e, mapping, composition, id_, A)

for _ in range(Q):
    query = input()
    if query[0] == "0":
        l, r, b, c = map(int, query[1:].split())
        segtree.apply(l, r, (b, c))
    if query[0] == "1":
        l, r = map(int, query[1:].split())
        print(segtree.prod(l, r)[0])
