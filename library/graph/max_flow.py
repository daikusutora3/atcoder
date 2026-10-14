from collections import namedtuple


class MFGraph:
    """非再帰 Dinic。頂点は 0-indexed、容量は非負整数。

    計算量: V は頂点数、E は追加した辺数。構築 O(V)、add_edge はならし O(1)、flow は一般に O(V^2 E)。
    edge_flow/get_edge は O(1)、edges は O(E)、min_cut は O(V + E)。空間 O(V + E)。

    Source: https://github.com/daikusutora3/atcoder
    """

    Edge = namedtuple("Edge", "src dst cap flow")

    def __init__(self, n):
        """計算量: 時間・空間 O(n)。"""
        assert n >= 0
        self.n = n
        self.g = [[] for _ in range(n)]
        self.to = []
        self.cap = []

    def add_edge(self, src, dst, cap):
        """計算量: ならし時間・追加空間 O(1)。"""
        assert 0 <= src < self.n and 0 <= dst < self.n
        assert cap >= 0
        e = len(self.to)
        self.g[src].append(e)
        self.g[dst].append(e + 1)
        self.to.extend((dst, src))
        self.cap.extend((cap, 0))
        return e >> 1

    def edge_flow(self, i):
        """計算量: 時間・追加空間 O(1)。"""
        assert 0 <= i < len(self.to) // 2
        return self.cap[2 * i + 1]

    def get_edge(self, i):
        """計算量: 時間・追加空間 O(1)。"""
        assert 0 <= i < len(self.to) // 2
        e = 2 * i
        return self.Edge(self.to[e + 1], self.to[e],
                         self.cap[e] + self.cap[e + 1], self.cap[e + 1])

    def edges(self):
        """計算量: 時間・出力空間 O(E)。E は追加した辺数。"""
        return [self.get_edge(i) for i in range(len(self.to) // 2)]

    def flow(self, s, t, flow_limit=None):
        """計算量: 一般に時間 O(V^2 E)、追加空間 O(V)。V は頂点数、E は辺数。"""
        assert 0 <= s < self.n and 0 <= t < self.n and s != t
        n, g, to, cap = self.n, self.g, self.to, self.cap
        if flow_limit is None:
            flow_limit = sum(cap[e] for e in g[s])
        assert flow_limit >= 0
        total = 0
        while total < flow_limit:
            level = [-1] * n
            level[s] = 0
            que = [s]
            for v in que:
                lv = level[v] + 1
                for e in g[v]:
                    w = to[e]
                    if cap[e] and level[w] < 0:
                        level[w] = lv
                        que.append(w)
                # t の直前の層までは発見済みなので BFS を終了できる。
                if level[t] >= 0:
                    break
            if level[t] < 0:
                break

            it = [0] * n
            path = []
            v = s
            while total < flow_limit:
                if v == t:
                    f = flow_limit - total
                    for e in path:
                        if cap[e] < f:
                            f = cap[e]
                    for e in path:
                        cap[e] -= f
                        cap[e ^ 1] += f
                    total += f
                    path.clear()
                    v = s
                    continue

                adj = g[v]
                while it[v] < len(adj):
                    e = adj[it[v]]
                    if cap[e] and level[to[e]] == level[v] + 1:
                        path.append(e)
                        v = to[e]
                        break
                    it[v] += 1
                else:
                    # この層グラフで t に届かない頂点は再訪しない。
                    level[v] = -1
                    if not path:
                        break
                    v = to[path.pop() ^ 1]
                    it[v] += 1
        return total

    def min_cut(self, s):
        """計算量: 時間 O(V + E)、追加空間 O(V)。V は頂点数、E は辺数。"""
        assert 0 <= s < self.n
        seen = [False] * self.n
        seen[s] = True
        que = [s]
        for v in que:
            for e in self.g[v]:
                w = self.to[e]
                if self.cap[e] and not seen[w]:
                    seen[w] = True
                    que.append(w)
        return seen
