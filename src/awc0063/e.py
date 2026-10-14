from atcoder.lazysegtree import LazySegTree

id_ = -1
e = (0, -1, -1)


# valueの型: (ブロック数,　左端の色, 右端の色)
def op(x, y):
    return (x[0] + y[0] - (1 if x[2] == y[1] else 0), x[1], y[2])


# 上のブロックの作用素を下のブロックの値に伝播
def mapping(f, x):
    if f == -1:
        return x
    else:
        return (1, f, f)


# 上のブロックの作用素を下のブロックの作用素に伝播
def composition(f, g):
    return g if f == -1 else f


N, Q = map(int, input().split())
C = list(map(int, input().split()))
C = [(1, c, c) for c in C]
segtree = LazySegTree(op, e, mapping, composition, id_, C)

for _ in range(Q):
    query = input()
    if query[0] == "1":
        L, R, X = map(int, query[1:].split())
        segtree.apply(L - 1, R, X)
    if query[0] == "2":
        L, R = map(int, query[1:].split())
        print(segtree.prod(L - 1, R)[0])
