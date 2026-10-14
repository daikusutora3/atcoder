from atcoder.lazysegtree import LazySegTree

INF = float("inf")


def op(ele1, ele2):
    return max(ele1, ele2)


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


e = -INF
id_ = 0


N, M = map(int, input().split())
lra = [list(map(int, input().split())) for i in range(M)]
lra.sort(key=lambda x: x[1])
seg = LazySegTree(op, e, mapping, composition, id_, [0 for _ in range(N + 1)])


br = 1

for i in range(M):
    l, r, a = lra[i]
    bmax = seg.prod(0, br)
    if l < br:
        seg.apply(l, br, a)
        seg.apply(br, r + 1, bmax + a)
    else:
        seg.apply(l, r + 1, bmax + a)

    br = r + 1

print(seg.all_prod())
