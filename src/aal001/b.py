from atcoder.lazysegtree import LazySegTree

INF = float("inf")
id_ = 0
e = INF


def op(x, y):
    return min(x, y)


# 上のブロックの作用素を下のブロックの値に伝播
# f = (b, c)
def mapping(f, x):
    return x + f


# 上のブロックの作用素を下のブロックの作用素に伝播
def composition(f, g):
    return f + g


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = [a for a in A]
segtree = LazySegTree(op, e, mapping, composition, id_, A)

for _ in range(Q):
    query = input()
    if query[0] == "1":
        l, r, x = map(int, query[1:].split())
        segtree.apply(l - 1, r, x)
    if query[0] == "2":
        l, r = map(int, query[1:].split())
        print(segtree.prod(l - 1, r))
