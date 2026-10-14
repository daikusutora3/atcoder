import sys
from collections import deque

from sortedcontainers import SortedList

sys.setrecursionlimit(10**6)


def topological_sort(graph):
    n = len(graph)
    indeg = [0] * n

    for v in range(n):
        for to in graph[v]:
            indeg[to] += 1

    q = deque(v for v in range(n) if indeg[v] == 0)
    order = []

    while q:
        v = q.popleft()
        order.append(v)

        for to in graph[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)

    return order if len(order) == n else []


# https://tjkendev.github.io/procon-library/python/graph/scc.html
# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
from heapq import heappop, heappush


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


def is_ng(GP):
    res = False
    for gp in GP:
        if len(gp) > 1:
            res = True
    return res


N, M = map(int, input().split())
# N, M = randint(2, 2000), randint(1, 1000)
G = [SortedList() for i in range(N)]
GR = [SortedList() for i in range(N)]

X = 0
hp = []
ans_X = []
for _ in range(M):
    WKP = list(map(int, input().split()))
    W = WKP[0]
    # W = randint(1, 10**9)
    K = WKP[1]
    # K = randint(2, N)
    P = [p - 1 for p in WKP[2:]]
    # P = list(range(K))
    heappush(hp, [W, K, P])
    for i in range(K - 1):
        G[P[i]].add(P[i + 1])
        GR[P[i + 1]].add(P[i])
    label, group = scc(N, G, GR)
    G0, GP = construct(N, G, label, group)
    while is_ng(GP):
        W, K, P = heappop(hp)
        X = max(X, W)
        for i in range(K - 1):
            G[P[i]].remove(P[i + 1])
            GR[P[i + 1]].remove(P[i])
        label, group = scc(N, G, GR)
        G0, GP = construct(N, G, label, group)
    ans_X.append(X)

print(*ans_X)
print(*[v + 1 for v in topological_sort(G)])
