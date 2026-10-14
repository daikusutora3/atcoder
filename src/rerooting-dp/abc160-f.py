from collections import deque
from itertools import accumulate
from functools import reduce

MOD = 10**9 + 7


def build_fact(n, mod=MOD):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod

    invfact = [1] * (n + 1)
    invfact[n] = pow(fact[n], mod - 2, mod)  # フェルマーの小定理
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % mod

    return fact, invfact


def comb(n, k, fact, invfact, mod=MOD):
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % mod * invfact[n - k] % mod


N = int(input())

fact, invfact = build_fact(N)

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
dp = [{v: 1 for v in adj} for adj in tree]

# ------------------------------------------------------------
# 1. bottom-up: dp[u][v] = 1 + max( dp[x][u] (x != v) )
# ------------------------------------------------------------
for u in reversed(order):
    v = par[u]
    if v == -1:
        continue
    size_list = [dp_size[x][u] for x in tree[u] if x != v]
    size_sum = sum(size_list)
    dp_size[u][v] = 1 + size_sum
    dp[u][v] = reduce(
        lambda acc, v: (acc * v) % MOD,
        [(dp[x][u] * invfact[dp_size[x][u]]) % MOD for x in tree[u] if x != v]
        + [fact[size_sum]],
        1,
    )

pref_size = [[] for _ in range(N)]
suf_size = [[] for _ in range(N)]
pref = [[] for _ in range(N)]
suf = [[] for _ in range(N)]

for u in range(N):
    vals = [dp_size[x][u] for x in children[u]]
    pref_size[u] = [0] + list(accumulate(vals))
    suf_size[u] = list(accumulate(reversed(vals)))[::-1] + [0]
    vals = [(dp[x][u] * invfact[dp_size[x][u]]) % MOD for x in children[u]]
    pref[u] = [1] + list(accumulate(vals, func=lambda x, y: (x * y) % MOD))
    suf[u] = list(accumulate(reversed(vals), func=lambda x, y: (x * y) % MOD))[::-1] + [
        1
    ]

for u in order:
    p = par[u]
    par_in_size = dp_size[p][u] if p != -1 else 0
    par_in = (dp[p][u] * invfact[par_in_size]) % MOD if p != -1 else 1
    for i, v in enumerate(children[u]):
        dp_size[u][v] = 1 + sum([par_in_size, pref_size[u][i], suf_size[u][i + 1]])
        dp[u][v] = reduce(
            lambda acc, v: (acc * v) % MOD,
            [par_in, pref[u][i], suf[u][i + 1]] + [fact[dp_size[u][v] - 1]],
            1,
        )

ans = []
for v in range(N):
    ans.append(
        reduce(
            lambda acc, v: (acc * v) % MOD,
            [(dp[x][v] * invfact[dp_size[x][v]]) % MOD for x in tree[v]]
            + [fact[sum(dp_size[x][v] for x in tree[v])]],
            1,
        )
    )

print(*ans, sep="\n")
