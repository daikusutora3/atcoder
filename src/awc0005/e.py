from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

segtree = SegTree(max, -1, A)

ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(segtree.prod(l - 1, r))

print(*ans, sep="\n")
