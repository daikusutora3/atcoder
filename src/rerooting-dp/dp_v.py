from collections import deque
from itertools import accumulate

N, M = map(int, input().split())

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
dp = [{v: 1 for v in adj} for adj in tree]

# ------------------------------------------------------------
# 1. bottom-up: dp[u][v] = 1 + max( dp[x][u] (x != v) )
# ------------------------------------------------------------
for u in reversed(order):
    v = par[u]
    if v == -1:
        continue
    for x in tree[u]:
        if x != v:
            dp[u][v] = (dp[u][v] * (dp[x][u] + 1)) % M

pref = [[] for _ in range(N)]
suf = [[] for _ in range(N)]

for u in range(N):
    vals = [dp[v][u] + 1 for v in children[u]]
    pref[u] = [1] + list(accumulate(vals, func=lambda x, y: (x * y) % M))
    suf[u] = list(accumulate(reversed(vals), func=lambda x, y: (x * y) % M))[::-1] + [1]


for u in order:
    p = par[u]
    par_in = dp[p][u] + 1 if p != -1 else 1
    for i, v in enumerate(children[u]):
        # print(f"{u} -> {v}: {par_in}, {pref[u][i]}, {suf[u][i + 1]}")
        dp[u][v] = dp[u][v] * (par_in * pref[u][i] * suf[u][i + 1]) % M

ans = []
for v in range(N):
    res = 1
    for x in tree[v]:
        res = (res * (dp[x][v] + 1)) % M
    ans.append(res)

print(*ans, sep="\n")
