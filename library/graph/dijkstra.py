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
