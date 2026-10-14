# https://atcoder.jp/contests/practice2/tasks/practice2_b

from atcoder.lazysegtree import LazySegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
INF = 1 << 63


def op(ele1, ele2):
    return min(ele1, ele2)


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


e = INF
id_ = 0

seg = LazySegTree(op, e, mapping, composition, id_, A)

for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, L, R, X = map(int, query.split())
        seg.apply(L - 1, R, X)
    else:
        _, P = map(int, query.split())
        print(seg.get(P - 1))
