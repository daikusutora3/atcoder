import sys
from collections import deque

sys.setrecursionlimit(10**6)


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

input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for i in range(N)]
GR = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    GR[b - 1].append(a - 1)

Q = int(input())
label, group = scc(N, G, GR)
G0, GP = construct(N, G, label, group)
painted = [0 for _ in range(label)]
G0_reversed = [set() for _ in range(label)]

for i in range(label):
    for u in G0[i]:
        G0_reversed[u].add(i)

for _ in range(Q):
    query = tuple(map(int, input().split()))
    v = query[1] - 1
    if query[0] == 1:
        queue = deque([group[v]])
        while queue:
            v = queue.popleft()
            if painted[v]:
                continue
            painted[v] = 1
            for i in G0_reversed[v]:
                if painted[i] == 0:
                    queue.append(i)
        queue = []
    else:
        print("Yes" if painted[group[v]] == 1 else "No")
