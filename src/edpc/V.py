from collections import deque


N, M = map(int, input().split())
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    tree[s].append(t)
    tree[t].append(s)

# ------------------------------------------------------------
# 0. 根付き木にして、親 par と BFS 順 order と children を作る
# ------------------------------------------------------------
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
# [白のときの場合の数, 黒のときの場合の数]
dp = [{v: [1, 1] for v in adj} for adj in tree]

# ------------------------------------------------------------
# 1. bottom-up
# ------------------------------------------------------------
for u in reversed(order):
    v = par[u]
    if v == -1:
        continue
    for x in tree[u]:
        if x == par[u]:
            continue
        dp[u][v][0] *= dp[x][u][0]
        dp[u][v][1] *= dp[x][u][0] + dp[x][u][1]
        dp[u][v][0] %= M
        dp[u][v][1] %= M

# ------------------------------------------------------------
# 2. prefix / suffix
# ------------------------------------------------------------
pref_w = [[1 for __ in range(len(children[u]) + 1)] for u in range(N)]
pref_bw = [[1 for __ in range(len(children[u]) + 1)] for u in range(N)]
suf_w = [[1 for __ in range(len(children[u]) + 1)] for u in range(N)]
suf_bw = [[1 for __ in range(len(children[u]) + 1)] for u in range(N)]

for u in range(N):
    vals_w = [dp[v][u][0] for v in children[u]]
    vals_bw = [dp[v][u][0] + dp[v][u][1] for v in children[u]]
    # children[u][:i] から来る組合せ
    for i in range(len(children[u])):
        pref_w[u][i + 1] = pref_w[u][i] * vals_w[i]
        pref_bw[u][i + 1] = pref_bw[u][i] * vals_bw[i]
        pref_w[u][i + 1] %= M
        pref_bw[u][i + 1] %= M
    # children[u][i+1:] から来る組合せ
    for i in range(len(children[u]) - 1, -1, -1):
        suf_w[u][i] = suf_w[u][i + 1] * vals_w[i]
        suf_bw[u][i] = suf_bw[u][i + 1] * vals_bw[i]
        suf_w[u][i + 1] %= M
        suf_bw[u][i + 1] %= M

# ------------------------------------------------------------
# 3. top-down: dp[u][v] = 1 + max( par_in, pref[u][i], suf[u][i+1] )
# ------------------------------------------------------------
for u in order:
    p = par[u]
    par_in_w = dp[p][u][0] if p != -1 else 1
    par_in_bw = (dp[p][u][0] + dp[p][u][1]) if p != -1 else 1
    for i, v in enumerate(children[u]):
        dp[u][v][0] = par_in_w * pref_w[u][i] * suf_w[u][i + 1]
        dp[u][v][1] = par_in_bw * pref_bw[u][i] * suf_bw[u][i + 1]

for v in range(N):
    ans = 1
    for x in tree[v]:
        ans *= dp[x][v][0] + dp[x][v][1]
        ans %= M
    print(ans)
