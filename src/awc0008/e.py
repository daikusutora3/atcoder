from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

segtree_ma = SegTree(max, -(10**10), A)
segtree_mi = SegTree(min, 10**10, A)

ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(segtree_ma.prod(l - 1, r) - segtree_mi.prod(l - 1, r))

print(*ans, sep="\n")
