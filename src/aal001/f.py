from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))


class S:
    def __init__(self, a):
        self.len = 1 if a != -1 else 0
        self.pref = [a, 1]
        self.suf = [a, 1]
        self.ans = 1


# [
# len
# [左端の数字, その数字がprefで何個連続しているか],
# [右端の数字, その数字がsufで何個連続しているか],
# 今見ている範囲で最大の連続文字の長さ,
# ]
def op(a: S, b: S):
    if a.len == 0:
        return b
    if b.len == 0:
        return a
    p = S(-1)
    p.len = a.len + b.len
    if a.pref[1] == a.len and a.pref[0] == b.pref[0]:
        p.pref = [a.pref[0], a.pref[1] + b.pref[1]]
    else:
        p.pref = [a.pref[0], a.pref[1]]
    if b.suf[1] == b.len and a.suf[0] == b.suf[0]:
        p.suf = [b.suf[0], b.suf[1] + a.suf[1]]
    else:
        p.suf = [b.suf[0], b.suf[1]]
    if a.suf[0] == b.pref[0]:
        p.ans = max(p.ans, a.suf[1] + b.pref[1])
    p.ans = max(p.ans, a.ans, b.ans)
    return p


segtree = SegTree(
    op,
    S(-1),
    [S(a) for a in A],
)

for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        i, x = a, b
        segtree.set(i - 1, S(x))
    else:
        l, r = a, b
        res = segtree.prod(l - 1, r)
        print(res.ans)
