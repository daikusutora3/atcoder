from atcoder.segtree import SegTree

N, K = map(int, input().split())
A = list(map(int, input().split()))

segtree = SegTree(min, float("inf"), [float("inf") for _ in range(N)])
segtree.set(0, A[0])
for i in range(1, N):
    p = A[i] + segtree.prod(max(0, i - K), i)
    segtree.set(i, p)


print(segtree.get(N - 1))
