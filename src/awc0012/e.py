from atcoder.segtree import SegTree


N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [-(10**10) for i in range(N)]
dp[0] = A[0]
segtree = SegTree(max, -(10**20), dp)

for i in range(1, N):
    l, r = max(0, i - K), max(0, i - 1)
    dp[i] = segtree.prod(l, r + 1) + A[i]
    segtree.set(i, dp[i])

print(dp[N - 1])
