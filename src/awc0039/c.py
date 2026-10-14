from atcoder.segtree import SegTree

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

segtree_A = SegTree(lambda x, y: x + y, 0, A)
segtree_B = SegTree(lambda x, y: x + y, 0, B)

ans = 0
for l in range(N):
    r = segtree_B.max_right(l, lambda x: x <= K)
    ans = max(ans, segtree_A.prod(l, r))

print(ans)
