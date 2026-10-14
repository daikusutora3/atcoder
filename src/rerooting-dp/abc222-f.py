from collections import deque
from itertools import accumulate

N = int(input())

tree = [[] for _ in range(N)]
for _ in range(N - 1):
    s, t, c = map(int, input().split())
    tree[s - 1].append((t - 1, c))
    tree[t - 1].append((s - 1, c))

D = list(map(int, input().split()))

par = [(-1, 0)] * N
order = []
children = [[] for _ in range(N)]
root = 0
q = deque([root])

while q:
    u = q.popleft()
    order.append(u)
    for v, c in tree[u]:
        if v == par[u][0]:
            continue
        par[v] = (u, c)
        children[u].append((v, c))
        q.append(v)

# dp[u][v] = 有向辺 u -> v に載せる値
dp = [{v: 0 for v, _ in adj} for adj in tree]

# ------------------------------------------------------------
# 1. bottom-up: dp[u][v] = 1 + max( dp[x][u] (x != v) )
# ------------------------------------------------------------
for u in reversed(order):
    v, par_c = par[u]
    if v == -1:
        continue
    dp[u][v] = par_c + max([dp[x][u] for x, c in tree[u] if x != v] + [D[u]])

pref = [[] for _ in range(N)]
suf = [[] for _ in range(N)]

for u in range(N):
    vals = [dp[v][u] for v, c in children[u]]
    pref[u] = [0] + list(accumulate(vals, func=max))
    suf[u] = list(accumulate(reversed(vals), func=max))[::-1] + [0]


for u in order:
    p, par_c = par[u]
    par_in = dp[p][u] if p != -1 else 0
    for i, (v, c) in enumerate(children[u]):
        dp[u][v] = c + max(par_in, pref[u][i], suf[u][i + 1], D[u])

ans = [max(dp[x][v] for x, c in tree[v]) for v in range(N)]
print(*ans, sep="\n")
