from heapq import heappop, heappush


def dijkstra(s, graph, inf=float("inf")):
    dist = [inf] * len(graph)
    dist[s] = 0
    que = [(0, s)]
    while que:
        cost, v = heappop(que)
        if cost != dist[v]:
            continue
        for to, w in graph[v]:
            nd = cost + w
            if nd < dist[to]:
                dist[to] = nd
                heappush(que, (nd, to))
    return dist


N, M, K, T = map(int, input().split())
graph = [[] for i in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))

SP = []
S = set()
for _ in range(K):
    l = list(map(int, input().split()))
    SP.append([set(l[1:-1]), l[-1]])
    SP[-1][0] = {s - 1 for s in SP[-1][0]}
    S |= SP[-1][0]

S = sorted(S)
dist_table = []
for s in S:
    dist_table.append(dijkstra(s, graph))

dist = dijkstra(0, graph)
dp = [[float("inf") for i in range(len(S))] for bit in range(2 ** (len(S)))]

for i in range(len(S)):
    dp[1 << i][i] = dist[S[i]]

for bit in range(2 ** (len(S))):
    for v in range(len(S)):
        for nv in range(len(S)):
            if bit >> v & 1:
                # 頂点u -> 頂点vに移動する
                # print(
                #     f"({str(bin(bit))[2:]}, {v}) -> ({str(bin(bit | (1 << nv)))[2:]}, {nv})"
                # )
                # print(dp[bit | (1 << nv)][nv], dp[bit][v] + dist_table[v][S[nv]])
                dp[bit | (1 << nv)][nv] = min(
                    dp[bit | (1 << nv)][nv], dp[bit][v] + dist_table[v][S[nv]]
                )

ans = 0
for bit in range(2 ** (len(S))):
    for v in range(len(S)):
        if dp[bit][v] > T:
            continue
        # 上記以外のときはbitの集合に対して移動時間T以下で到達できる
        bit_set = set()
        res = 0
        for i in range(len(S)):
            if bit >> i & 1:
                bit_set.add(S[i])
        for s, p in SP:
            if s <= bit_set:
                res += p
        ans = max(ans, res)

print(ans)


# 4 5 3 7
# 1 2 7
# 2 3 3
# 1 4 10
# 3 4 1
# 1 3 1
# 1 2 100
# 2 2 3 300
# 1 4 500
