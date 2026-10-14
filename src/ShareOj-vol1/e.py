import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# https://tjkendev.github.io/procon-library/python/graph/scc.html
# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0] * N
    group = [None] * N

    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)

    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0] * N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group


# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP


# =========================


class ModComb:
    """素数 mod における階乗・順列・二項係数を前計算する。"""

    def __init__(self, max_n, mod):
        if max_n < 0:
            raise ValueError("max_n must be non-negative")
        if mod <= 1:
            raise ValueError("mod must be greater than 1")
        if max_n >= mod:
            raise ValueError("max_n must be smaller than mod")

        self.max_n = max_n
        self.mod = mod

        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % mod

        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
        for i in range(max_n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % mod

        self.fact = fact
        self.inv_fact = inv_fact

    def comb(self, n, k):
        """nCk mod mod を返す。k が範囲外なら 0。"""
        if n < 0:
            return 0
        if n > self.max_n:
            raise ValueError("n exceeds max_n")
        if k < 0 or k > n:
            return 0
        return (
            self.fact[n] * self.inv_fact[k] % self.mod * self.inv_fact[n - k] % self.mod
        )

    def perm(self, n, k):
        """nPk mod mod を返す。k が範囲外なら 0。"""
        if n < 0:
            return 0
        if n > self.max_n:
            raise ValueError("n exceeds max_n")
        if k < 0 or k > n:
            return 0
        return self.fact[n] * self.inv_fact[n - k] % self.mod


MOD = 998244353
mc = ModComb(200001, MOD)


def solve():
    N, M = map(int, input().split())
    G = [[] for i in range(N)]
    GR = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        GR[B - 1].append(A - 1)
    label, group = scc(N, G, GR)
    G0, GP = construct(N, G, label, group)
    in_deg = [0 for i in range(label)]
    for v in range(label):
        for nv in G0[v]:
            in_deg[nv] += 1
    cnt = [0 for v in range(label)]
    for v in range(label):
        if in_deg[v] == 0:
            for i in range(len(GP[v])):
                cnt[v] += mc.comb(len(GP[v]), i)
                cnt[v] %= MOD
        else:
            for i in range(len(GP[v]) + 1):
                cnt[v] += mc.comb(len(GP[v]), i)
                cnt[v] %= MOD
    ans = 1
    for c in cnt:
        ans *= c
        ans %= MOD
    print(ans)


T = int(input())
for _ in range(T):
    solve()
