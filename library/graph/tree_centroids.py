def tree_centroids(graph):
    """無向木の重心を1頂点または隣り合う2頂点の配列で返す。

    計算量: 時間 O(N)、追加空間 O(N)。N は頂点数。
    空でない連結な単純無向木を渡す。結果の順序は未規定。
    重心は、除去後の各連結成分の頂点数が N/2 以下になる頂点。

    Source: https://github.com/daikusutora3/atcoder
    """
    n = len(graph)
    parent = [-1] * n
    order = [0]
    for v in order:
        for to in graph[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            order.append(to)

    size = [1] * n
    centroids = []
    for v in reversed(order):
        largest = 0
        for to in graph[v]:
            if to == parent[v]:
                continue
            size[v] += size[to]
            largest = max(largest, size[to])
        largest = max(largest, n - size[v])
        if largest * 2 <= n:
            centroids.append(v)
    return centroids
