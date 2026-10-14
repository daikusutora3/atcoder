from heapq import heappop, heappush


def dijkstra(s, graph, inf=float("inf")):
    """Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/graph/dijkstra.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/graph/dijkstra.md"""
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
