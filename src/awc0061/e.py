from bisect import bisect_left, bisect_right
from atcoder.segtree import SegTree


def compress(values):
    """(comp, vals, idx) を返す。

    comp: values と同じ順序・長さの圧縮後リスト
    vals: values に登場する値を昇順に重複除去したリスト
    idx: 元の値から圧縮後 index への辞書
    """
    vals = sorted(set(values))
    idx = {x: i for i, x in enumerate(vals)}
    comp = [idx[x] for x in values]
    return comp, vals, idx


N, D = map(int, input().split())
H = list(map(int, input().split()))
segtree = SegTree(max, 0, [0 for i in range(N + 1)])

_, i2v, v2i = compress(H)

for i in range(N):
    bl = bisect_left(i2v, H[i] - D)
    br = bisect_right(i2v, H[i] + D)
    segtree.set(v2i[H[i]], segtree.prod(bl, br) + 1)
    # for i in range(N + 1):
    #     print(segtree.get(i), end=" ")
    # print()

print(segtree.all_prod())
