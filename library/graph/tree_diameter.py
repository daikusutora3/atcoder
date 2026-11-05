from collections import deque


def tree_diameter(graph):
    """重みなし無向木の直径を (辺数, 両端を含む頂点列) で返す。

    計算量: 時間 O(N)、追加空間 O(N)。N は頂点数。
    空でない連結な単純無向木を渡す。直径が複数ならいずれか1本を返す。

    Source: https://github.com/daikusutora3/atcoder
    """
    def search(s):
        """始点からの最遠頂点・距離配列・親配列を時間 O(N)、空間 O(N) で求める。"""
        dist = [-1] * len(graph)
        parent = [-1] * len(graph)
        dist[s] = 0
        que = deque([s])
        v = s
        while que:
            v = que.popleft()
            for to in graph[v]:
                if dist[to] != -1:
                    continue
                dist[to] = dist[v] + 1
                parent[to] = v
                que.append(to)
        return v, dist, parent

    s, _, _ = search(0)
    t, dist, parent = search(s)
    path = []
    v = t
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
    return dist[t], path


def tree_centers(graph):
    """重みなし無向木の中心を1頂点または隣り合う2頂点の配列で返す。

    計算量: 時間 O(N)、追加空間 O(N)。N は頂点数。
    入力の前提は tree_diameter と同じ。中心は最大距離（離心度）が最小の頂点。

    Source: https://github.com/daikusutora3/atcoder
    """
    diameter, path = tree_diameter(graph)
    return path[diameter // 2 : diameter // 2 + 1 + diameter % 2]
