from collections import deque
from itertools import accumulate

N = int(input())


id = [{} for _ in range(N)]
tree = [[] for _ in range(N)]
cost = [0 for _ in range(2 * N - 2)]
for i in range(N - 1):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    tree[s].append(t)
    tree[t].append(s)
    id[s][t] = i
    id[t][s] = i + N - 1
    cost[id[s][t]] = i + 1
    cost[id[t][s]] = i + 1

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

# dp1[id[u][v]] = 有向辺 u -> v に載せる値
dp1 = [0 for i in range(2 * N - 2)]
dp2 = [0 for i in range(2 * N - 2)]

# ------------------------------------------------------------
# 1. bottom-up: dp1[id[u][v]] = 1 + max( dp1[id[x][u]] (x != v) )
# ------------------------------------------------------------
for u in reversed(order):
    v = par[u]
    if v == -1:
        continue
    dp1[id[u][v]] = 1 + sum(dp1[id[x][u]] for x in tree[u] if x != v)
    dp2[id[u][v]] = sum(dp2[id[x][u]] for x in tree[u] if x != v)
    if dp1[id[u][v]] <= N // 2:
        dp2[id[u][v]] += cost[id[u][v]]

# ------------------------------------------------------------
# 2. prefix / suffix
# ------------------------------------------------------------
pref1 = [[] for _ in range(N)]
suf1 = [[] for _ in range(N)]
pref2 = [[] for _ in range(N)]
suf2 = [[] for _ in range(N)]

for u in range(N):
    vals1 = [dp1[id[v][u]] for v in children[u]]
    vals2 = [dp2[id[v][u]] for v in children[u]]
    # pref1[u][i] = children[u][:i] から来る最大値
    pref1[u] = [0] + list(accumulate(vals1, lambda x, y: x + y))
    pref2[u] = [0] + list(accumulate(vals2, lambda x, y: x + y))
    # suf1[u][i+1] = children[u][i+1:] から来る最大値
    suf1[u] = list(accumulate(reversed(vals1), lambda x, y: x + y))[::-1] + [0]
    suf2[u] = list(accumulate(reversed(vals2), lambda x, y: x + y))[::-1] + [0]

# ------------------------------------------------------------
# 3. top-down: dp1[id[u][v]] = 1 + sun( par_in, pref1[u][i], suf1[u][i+1] )
# ------------------------------------------------------------
for u in order:
    p = par[u]
    par_in1 = dp1[id[p][u]] if p != -1 else 0
    par_in2 = dp2[id[p][u]] if p != -1 else 0
    for i, v in enumerate(children[u]):
        dp1[id[u][v]] = 1 + par_in1 + pref1[u][i] + suf1[u][i + 1]
        dp2[id[u][v]] = par_in2 + pref2[u][i] + suf2[u][i + 1]
        if dp1[id[u][v]] <= N // 2:
            dp2[id[u][v]] += cost[id[u][v]]

ans = [sum(dp2[id[x][v]] for x in tree[v]) for v in range(N)]
print(*ans)
