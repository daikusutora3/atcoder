from atcoder.segtree import SegTree

INF = float("inf")


class S:
    global INF  # noqa: PLW0602

    def __init__(self, a):
        if a == INF:
            self.left = 0
            self.right = 0
            self.last = 0
        else:
            self.left = min(0, a)
            self.right = max(a, 0)
            self.last = a


def op(a: S, b: S):
    res = S(INF)
    res.left = min(0, a.left, a.last + b.left)
    res.right = max(0, a.right, a.last + b.right)
    res.last = a.last + b.last
    return res


N = int(input())
A = list(map(int, input().split()))

segtree = SegTree(
    op,
    S(INF),
    [S(a) for a in A],
)


res = segtree.all_prod()
ans = abs(res.left) + abs(res.right) + 1
for k in range(N):
    segtree.set(k, S(-A[k]))
    res = segtree.all_prod()
    ans = max(ans, abs(res.left) + abs(res.right) + 1)
    segtree.set(k, S(A[k]))

print(ans)
