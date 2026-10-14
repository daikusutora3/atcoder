from atcoder.lazysegtree import LazySegTree


N, Q = map(int, input().split())
A = list(map(int, input().split()))

id_ = 0
e = 0


# valueの型
def op(x, y):
    return x + y


# 上のブロックの作用素を下のブロックの値に伝播
def mapping(f, x):
    return x + f


# 上のブロックの作用素を下のブロックの作用素に伝播
def composition(f, g):
    return f + g


segtree = LazySegTree(op, e, mapping, composition, id_, A)

ans = 0
for i in range(N - 1):
    ans += abs(A[i] - A[i + 1])

for _ in range(Q):
    L, R, V = map(int, input().split())
    L, R = L - 1, R - 1
    if L > 0:
        A_L = segtree.prod(L, L + 1)
        A_Lm1 = segtree.prod(L - 1, L)
        before = abs(A_L - A_Lm1)
        after = abs((A_L + V) - A_Lm1)
        ans += after - before
    if R < N - 1:
        A_R = segtree.prod(R, R + 1)
        A_Ra1 = segtree.prod(R + 1, R + 2)
        before = abs(A_R - A_Ra1)
        after = abs((A_R + V) - A_Ra1)
        ans += after - before
    segtree.apply(L, R + 1, V)
    print(ans)
