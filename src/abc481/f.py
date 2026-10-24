from heapq import heapify, heappop, heappush


def dijkstra(s, graph, inf=float("inf"), mod=998244353):
    """計算量: 時間 O(V + E log(E + 2))、追加空間 O(V + E)。V は頂点数、E は辺数。重みは非負。

    Source: https://github.com/daikusutora3/atcoder
    """
    # dist[i] = (a, b) = a*mod + b
    dist = [[inf, inf]] * len(graph)
    # rank
    dist[s] = [0]
    # (前の頂点のrank, 辺のコスト, 今の頂点, 答え)
    que = []
    for to, w in graph[0]:
        que.append((0, w, to, 0))
    heapify(que)
    rank = 0
    br = None
    bc = None
    visited = [0 for i in range(N)]
    res = [0 for i in range(N)]

    while que:
        r, c, v, ans = heappop(que)
        if visited[v]:
            continue
        visited[v] = 1
        if br == r and bc == c:
            pass
        else:
            rank += 1
            br = r
            bc = c
        dist[v] = rank
        res[v] = (ans * 10 + c) % mod
        for to, w in graph[v]:
            if not visited[to]:
                heappush(que, (rank, w, to, res[v]))
    return res


N, M = map(int, input().split())
graph = [[] for i in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append((B, C))

res = dijkstra(0, graph)
for i in range(1, N):
    print(res[i])
