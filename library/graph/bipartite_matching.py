class BipartiteMatching:
    """辺を追加して solve() で最大マッチング数、pairs() で対応を得る。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/graph/bipartite_matching.md
    """

    def __init__(self, n, m):
        """Docs: https://github.com/daikusutora3/atcoder/blob/main/library/graph/bipartite_matching.md"""
        assert n >= 0 and m >= 0
        self._adj = [[] for _ in range(n)]
        self._m = m
        self._match = None
        self._size = 0

    def add_edge(self, u, v):
        """Docs: https://github.com/daikusutora3/atcoder/blob/main/library/graph/bipartite_matching.md"""
        assert 0 <= u < len(self._adj) and 0 <= v < self._m
        self._adj[u].append(v)
        self._match = None

    def solve(self):
        """Docs: https://github.com/daikusutora3/atcoder/blob/main/library/graph/bipartite_matching.md"""
        if self._match is None:
            self._match = bipartite_matching(self._adj, self._m)
            self._size = sum(v >= 0 for v in self._match)
        return self._size

    def pairs(self):
        """Docs: https://github.com/daikusutora3/atcoder/blob/main/library/graph/bipartite_matching.md"""
        self.solve()
        return [(u, v) for u, v in enumerate(self._match) if v >= 0]


def bipartite_matching(adj, m):
    """非再帰 Hopcroft–Karp。左頂点ごとの相手（未対応は -1）を返す。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/graph/bipartite_matching.md
    """
    assert m >= 0
    n = len(adj)
    left = [-1] * n
    right = [-1] * m
    # 長さ1の増加路を先に処理する。
    for u, row in enumerate(adj):
        for v in row:
            if right[v] < 0:
                left[u] = v
                right[v] = u
                break
    while True:
        dist = [-1] * n
        que = []
        for u in range(n):
            if left[u] < 0:
                dist[u] = 0
                que.append(u)
        depth = n
        for u in que:
            if dist[u] >= depth:
                break
            for v in adj[u]:
                w = right[v]
                if w < 0:
                    depth = dist[u]
                elif dist[w] < 0:
                    dist[w] = dist[u] + 1
                    que.append(w)
        if depth == n:
            return left
        it = [0] * n
        for root in que:
            if dist[root] != 0 or left[root] >= 0:
                continue
            stack = [root]
            while stack:
                u = stack[-1]
                row = adj[u]
                while it[u] < len(row):
                    v = row[it[u]]
                    it[u] += 1
                    w = right[v]
                    if w < 0:
                        if dist[u] != depth:
                            continue
                        for x in reversed(stack):
                            old = left[x]
                            left[x] = v
                            right[v] = x
                            v = old
                        stack.clear()
                        break
                    if dist[w] == dist[u] + 1 and dist[w] <= depth:
                        stack.append(w)
                        break
                else:
                    dist[u] = -1
                    stack.pop()
