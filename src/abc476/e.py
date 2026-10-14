from atcoder.segtree import SegTree

N, M = map(int, input().split())
P = list(map(int, input().split()))


def op(a, b):
    # minの更新をしたい
    min = -1
    min_i = -1
    if a[0] < b[0]:
        min = a[0]
        min_i = a[1]
    else:
        min = b[0]
        min_i = b[1]
    # maxの更新をしたい
    max = -1
    max_i = -1
    if a[2] > b[2]:
        max = a[2]
        max_i = a[3]
    else:
        max = b[2]
        max_i = b[3]
    return [min, min_i, max, max_i]


INF = float("inf")
# [min, min_ind, max, max_ind]
segtree = SegTree(op, [INF, -1, -INF, -1], [[P[i], i, P[i], i] for i in range(N)])


for _ in range(M):
    L, R = map(int, input().split())
    min, min_ind, max, max_ind = segtree.prod(L - 1, R)
    segtree.set(min_ind, [max, min_ind, max, min_ind])
    segtree.set(max_ind, [min, max_ind, min, max_ind])

ans = []
for i in range(N):
    ans.append(segtree.get(i)[0])


print(*ans)
