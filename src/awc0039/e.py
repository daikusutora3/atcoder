from collections import deque

from atcoder.segtree import SegTree

N, M, Q, K = map(int, input().split())
SD = [list(map(int, input().split())) for i in range(M)]
queries = [list(map(int, input().split())) for _ in range(Q)]
queries = [(q[0], q[1], q[2], qi) for qi, q in enumerate(queries)]

segtree = SegTree(lambda x, y: x + y, 0, [0 for i in range(N)])

SD.sort(key=lambda x: -x[1])
SD = deque(SD)
queries.sort(key=lambda x: -x[2])

ans = [0 for i in range(Q)]
for l, r, t, qi in queries:
    while len(SD) and SD[0][1] >= t:
        s, _ = SD.popleft()
        # print("add:", s, _)
        segtree.set(s - 1, segtree.get(s - 1) + 1)
    ans[qi] = max(0, segtree.prod(l - 1, r) - K)

print(*ans, sep="\n")
