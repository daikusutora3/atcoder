from atcoder.segtree import SegTree

N, K = map(int, input().split())
A = list(map(int, input().split()))


# x = [min, max]
def op(x, y):
    res = (min(x[0], y[0]), max(x[1], y[1]))
    return res


e = (float("inf"), -float("inf"))

A = [(a, a) for a in A]

segtree = SegTree(op, e, A)

cntK = 0
for l in range(N):
    r = segtree.max_right(l, lambda x: x[1] - x[0] <= K)
    cntK += r - l

cntK_1 = 0
for l in range(N):
    r = segtree.max_right(l, lambda x: x[1] - x[0] < K)
    cntK_1 += r - l

print(cntK - cntK_1)
