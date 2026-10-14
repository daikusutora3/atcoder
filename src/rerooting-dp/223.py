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
# [vをマッチングに使っているときのマッチング数の最大, vをマッチングに使っていないときのマッチング数の最大]
dp = [{v: [0, 0] for v in adj} for adj in tree]

# ------------------------------------------------------------
# 1. bottom-up: dp[u][v] = 1 + max( dp[x][u] (x != v) )
# ------------------------------------------------------------
for u in reversed(order):
    v = par[u]
    if v == -1:
        continue
    diff = float("inf")
    # print(f"===={u}====")
    for x in tree[u]:
        if x != v:
            if dp[x][u][0] - dp[x][u][1] < diff:
                diff = dp[x][u][0] - dp[x][u][1]
            dp[u][v][0] += max(dp[x][u])
            dp[u][v][1] += max(dp[x][u])
    # print(f"sum: {dp[u][v][1]}, diff: {diff}")
    dp[u][v][0] += 1 - diff if diff != float("inf") else 0
    # print(f"{u} -> {v}:{dp[u][v]}")

# print(dp)

pref = [[] for _ in range(N)]
suf = [[] for _ in range(N)]
pref_diff = [[] for _ in range(N)]
suf_diff = [[] for _ in range(N)]

for u in range(N):
    vals = [max(dp[v][u]) for v in children[u]]
    pref[u] = [0] + list(accumulate(vals))
    suf[u] = list(accumulate(reversed(vals)))[::-1] + [0]
    vals = [dp[v][u][0] - dp[v][u][1] for v in children[u]]
    pref_diff[u] = [float("inf")] + list(accumulate(vals, lambda x, y: min(x, y)))
    suf_diff[u] = list(accumulate(reversed(vals), lambda x, y: min(x, y)))[::-1] + [
        float("inf")
    ]


for u in order:
    p = par[u]
    par_in = max(dp[p][u]) if p != -1 else 0
    par_in_diff = dp[p][u][0] - dp[p][u][1] if p != -1 else float("inf")
    # print("par_in_diff", par_in_diff)
    for i, v in enumerate(children[u]):
        dp[u][v][0] = par_in + pref[u][i] + suf[u][i + 1]
        dp[u][v][1] = par_in + pref[u][i] + suf[u][i + 1]
        # print(f"sum: {dp[u][v][1]}, diff: {diff}")
        diff = min(pref_diff[u][i], suf_diff[u][i + 1], par_in_diff)
        # print(pref_diff[u][i], suf_diff[u][i + 1])
        dp[u][v][0] += 1 - diff if diff != float("inf") else 0
        # print(f"{u} -> {v}:{dp[u][v]}")


# print(dp)
ans = 0

MAX_MATCHING = 0
diff = float("inf")
for x in tree[v]:
    if dp[x][v][0] - dp[x][v][1] <= diff:
        diff = dp[x][v][0] - dp[x][v][1]
    MAX_MATCHING += max(dp[x][v])
MAX_MATCHING = max(
    MAX_MATCHING, MAX_MATCHING + (1 - diff if diff != float("inf") else 0)
)

for v in range(N):
    # print(f"==={v}===")
    res = 0
    for x in tree[v]:
        # print(f"{x} -> {v}: {dp[x][v]}")
        res += max(dp[x][v])
    if MAX_MATCHING == res and MAX_MATCHING != 0:
        ans += 1

print(ans)
