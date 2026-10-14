from heapq import heappop, heappush


def dijkstra(s, graph, inf=float("inf")):
    """計算量: 時間 O(V + E log(E + 2))、追加空間 O(V + E)。V は頂点数、E は辺数。重みは非負。

    Source: https://github.com/daikusutora3/atcoder
    """
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
