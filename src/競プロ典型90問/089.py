from collections import deque
from atcoder.fenwicktree import FenwickTree

mod = 10**9 + 7


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


N, K = map(int, input().split())
A = list(map(int, input().split()))

comp, vals, idx = compress(A)
comp = [c + 1 for c in comp]
fenwick = FenwickTree(N + 1)
r2l = [0 for i in range(N)]
queue = deque()
tentou = 0
for r in range(N):
    rt = fenwick.sum(comp[r] + 1, N + 1)
    tentou += rt
    queue.append(r)
    fenwick.add(comp[r], 1)
    while len(queue) and tentou > K:
        l = queue.popleft()
        tentou -= fenwick.sum(0, comp[l])
        fenwick.add(comp[l], -1)
    r2l[r] = queue[0]

dp = [0 for i in range(N + 1)]
rui_dp = [0 for i in range(N + 1)]
dp[0] = 1

for r in range(1, N + 1):
    l = r2l[r - 1]
    rui_dp[r] += dp[r - 1] + rui_dp[r - 1]
    rui_dp[r] %= mod
    dp[r] = rui_dp[r] - rui_dp[l]
    dp[r] %= mod

print(dp[N])
