from atcoder.segtree import SegTree

N = int(input())
H = list(map(int, input().split()))

segtree = SegTree(max, -float("inf"), H)
segtree_min = SegTree(min, float("inf"), H)

ans = 0
for i in range(N):
    r = segtree.max_right(i, lambda x: x <= H[i])
    if r == N:
        continue
    ans += segtree_min.prod(i, r + 1)

print(ans)
