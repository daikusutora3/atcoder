from collections import deque
from itertools import accumulate

N = int(input())

tree = [[] for _ in range(N)]
for _ in range(N - 1):
    s, t = map(int, input().split())
    tree[s - 1].append(t - 1)
    tree[t - 1].append(s - 1)

par = [-1] * N
order = []
children = [[] for _ in range(N)]
root = 0
q = deque([root])

while q:
    u = q.popleft()
    order.append(u)
    for v in tree[u]:
        if v == par[u]:
            continue
        par[v] = u
        children[u].append(v)
        q.append(v)

# dp[u][v] = 有向辺 u -> v に載せる値
dp_size = [{v: 0 for v in adj} for adj in tree]
dp = [{v: 0 for v in adj} for adj in tree]

# ------------------------------------------------------------
# 1. bottom-up: dp[u][v] = 1 + max( dp[x][u] (x != v) )
# ------------------------------------------------------------
for u in reversed(order):
    v = par[u]
    if v == -1:
        continue
    dp_size[u][v] = 1 + sum([dp_size[x][u] for x in tree[u] if x != v])
    dp[u][v] = sum([dp[x][u] for x in tree[u] if x != v]) + dp_size[u][v]

pref_size = [[] for _ in range(N)]
suf_size = [[] for _ in range(N)]
pref = [[] for _ in range(N)]
suf = [[] for _ in range(N)]

for u in range(N):
    vals = [dp_size[v][u] for v in children[u]]
    pref_size[u] = [0] + list(accumulate(vals))
    suf_size[u] = list(accumulate(reversed(vals)))[::-1] + [0]
    vals = [dp[v][u] for v in children[u]]
    pref[u] = [0] + list(accumulate(vals))
    suf[u] = list(accumulate(reversed(vals)))[::-1] + [0]

for u in order:
    p = par[u]
    par_in_size = dp_size[p][u] if p != -1 else 0
    par_in = dp[p][u] if p != -1 else 0
    for i, v in enumerate(children[u]):
        dp_size[u][v] = 1 + sum([par_in_size, pref_size[u][i], suf_size[u][i + 1]])
        dp[u][v] = dp_size[u][v] + sum([par_in, pref[u][i], suf[u][i + 1]])

ans = []
for v in range(N):
    ans.append(sum([dp[x][v] for x in tree[v]]))

print(*ans, sep="\n")
