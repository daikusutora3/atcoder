from atcoder.segtree import SegTree

N, M, S = map(int, input().split())
segtree = SegTree(lambda a, b: a + b, 0, [1 for _ in range(N)])

S -= 1
for _ in range(M):
    segtree.set(S, 0)
    D = int(input())
    all_prod = segtree.all_prod()
    if D > all_prod:
        D %= all_prod
        if D == 0:
            D = all_prod
    prod_SN = segtree.prod(S, N)
    if D <= prod_SN:
        S = segtree.max_right(S, lambda x: x < D)
    else:
        S = segtree.max_right(0, lambda x: x < D - prod_SN)

print(S + 1)
