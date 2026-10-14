from heapq import heappop, heappush


def dijkstra(s, graph, inf=float("inf")):
    """Docs: https://github.com/daikusutora3/atcoder/blob/main/library/graph/dijkstra.md"""
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


N, M, K = map(int, input().split())
b = []
C = []
kiken = set()
for _ in range(M):
    bC = list(map(int, input().split()))
    b.append(bC[:-1])
    C.append(bC[-1])

for _ in range(K):
    F = list(map(int, input().split()))
    res = 0
    now = 1
    for f in F:
        res += f * now
        now *= 2
    kiken.add(res)


graph = [[] for i in range(2**N)]
for bit in range(2**N):
    if bit in kiken:
        continue
    for j in range(M):
        nbit = bit
        for i in range(N):
            if b[j][i]:
                nbit = nbit ^ (1 << i)
        graph[bit].append((nbit, C[j]))

dist = dijkstra(0, graph)
ans = dist[-1]
print(-1 if ans == float("inf") else dist[-1])
