from atcoder.segtree import SegTree

N = int(input())
S = input()


def op(x, y):
    need1, supply1 = x
    need2, supply2 = y
    need = need1 + max(0, need2 - supply1)
    supply = supply2 + max(0, -(need2 - supply1))
    return [need, supply]


# [need, supply]
segtree = SegTree(op, [0, 0], [[0, 1] if s == "A" else [1, 0] for s in S])
Q = int(input())

for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, i, c = query.split()
        i = int(i)
        segtree.set(i - 1, [0, 1] if c == "A" else [1, 0])
    else:
        _, l, r = map(int, query.split())
        need, _ = segtree.prod(l - 1, r)
        if need == 0:
            print("Yes")
        else:
            print("No")
