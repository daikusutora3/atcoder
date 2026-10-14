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


N, M = map(int, input().split())
INF = 2**60
graph = [[] for i in range(N)]

ans = 0
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))
    ans += w


odd_v = []

for i in range(N):
    if len(graph[i]) % 2 == 1:
        odd_v.append(i)

K = len(odd_v)
dp = [INF for i in range(2**K)]
dp[0] = 0

i_dist = []
for i in range(K):
    dist = dijkstra(odd_v[i], graph, inf=INF)
    i_dist.append(dist)

for bit in range(2**K):
    if not (bit.bit_count() % 2 == 0 and bit.bit_count() > 0):
        continue
    for i in range(K):
        for j in range(i + 1, K):
            if (bit >> i & 1) and (bit >> j & 1):
                dist = i_dist[i]
                b_bit = (bit & ~(1 << i)) & ~(1 << j)
                dp[bit] = min(dp[bit], dp[b_bit] + dist[odd_v[j]])


ans += dp[2**K - 1]
print(ans)
