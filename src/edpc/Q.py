from atcoder.segtree import SegTree

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

segtree = SegTree(max, 0, [0 for _ in range(N)])

for i in range(N):
    h, a = H[i], A[i]
    segtree.set(h - 1, segtree.prod(0, h - 1) + a)

print(segtree.all_prod())
