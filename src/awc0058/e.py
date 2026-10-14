from atcoder.segtree import SegTree


N, K = map(int, input().split())
A = list(map(int, input().split()))


segtree = SegTree(
    lambda a, b: [min(a[0], b[0]), max(a[1], b[1])],
    [float("inf"), -float("inf")],
    [[A[i], A[i]] for i in range(N)],
)

ans = 0
for l in range(N):
    r = segtree.max_right(l, lambda v: v[1] - v[0] <= K)
    ans = max(ans, r - l)

print(ans)
