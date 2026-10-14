from atcoder.segtree import SegTree

N = int(input())
Q = list(map(int, input().split()))

INF = float("inf")
segtree = SegTree(max, -INF, [0 for i in range(N)])
mod = 998244353
ans = 1
for i in range(N):
    if i > 0:
        ans *= i - segtree.prod(Q[i] - 1, N)
        ans %= mod
        # print(segtree.prod(Q[i] - 1, N), i)
    segtree.set(Q[i] - 1, i)

print(ans)
