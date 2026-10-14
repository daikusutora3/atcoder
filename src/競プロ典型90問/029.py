from atcoder.lazysegtree import LazySegTree

id_ = 0


# 値の2項演算
def op(value1, value2):
    return max(value1, value2)


# 上のブロックの作用素を下のブロックの値に伝播
def mapping(f, value):
    return value if f is id_ else f


# 上のブロックの作用素を下のブロックの作用素に伝播
def composition(f, g):
    return g if f is id_ else f


W, N = map(int, input().split())

e = -1
segtree = LazySegTree(op, e, mapping, composition, id_, [0 for w in range(W)])
for i in range(N):
    L, R = map(int, input().split())
    height = segtree.prod(L - 1, R)
    segtree.apply(L - 1, R, height + 1)
    print(height + 1)
