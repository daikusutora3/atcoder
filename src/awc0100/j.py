import sys
from collections import deque

sys.setrecursionlimit(10**6)


class LCA:
    def __init__(self, n, graph, root=0):
        """
        n     : 頂点数
        graph : 隣接リスト
        root  : 根にする頂点
        """

        self.n = n
        self.graph = graph
        self.root = root

        # LOG = 2^k <= n を満たす最大の k に少し余裕を持たせたもの
        self.LOG = max(1, (n - 1).bit_length())

        # parent[k][v] := 頂点 v の 2^k 個上の祖先
        self.parent = [[-1] * n for _ in range(self.LOG)]

        # depth[v] := 根からの深さ
        self.depth = [-1] * n

        # 根から BFS/DFS して、
        # parent[0][v]（1個上の親）と depth[v] を埋める
        self._build()

        # ダブリングテーブル構築
        self._doubling()

    def _build(self):
        """parent[0], depth を BFS で構築"""
        q = deque([self.root])
        self.depth[self.root] = 0
        self.parent[0][self.root] = -1

        while q:
            v = q.popleft()
            for nv in self.graph[v]:
                if self.depth[nv] != -1:
                    continue
                self.depth[nv] = self.depth[v] + 1
                self.parent[0][nv] = v
                q.append(nv)

    def _doubling(self):
        """parent[k][v] を構築"""
        for k in range(self.LOG - 1):
            for v in range(self.n):
                p = self.parent[k][v]
                if p == -1:
                    self.parent[k + 1][v] = -1
                else:
                    self.parent[k + 1][v] = self.parent[k][p]

    def kth_ancestor(self, v, k):
        """
        頂点 v の k 個上の祖先を返す
        存在しなければ -1
        """
        for i in range(self.LOG):
            if k >> i & 1:
                v = self.parent[i][v]
                if v == -1:
                    return -1
        return v

    def lca(self, u, v):
        """u, v の最近共通祖先を返す"""

        # 深さを揃える
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        u = self.kth_ancestor(u, diff)

        # 揃えた時点で一致したら、それが LCA
        if u == v:
            return u

        # 大きい方の 2^k から順に、
        # まだ一致しないなら両方まとめて上げる
        for k in range(self.LOG - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]

        # 1個上が LCA
        return self.parent[0][u]


N = int(input())
tree = [[] for i in range(N)]
edge_cost = [0 for i in range(N)]
for i in range(N - 1):
    P, W = map(int, input().split())
    tree[P - 1].append(i + 1)
    edge_cost[i + 1] = W

lca = LCA(N, tree)
Q = int(input())
v_cost = [0 for i in range(N)]
for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uv_lca = lca.lca(u, v)
    v_cost[uv_lca] -= 2
    v_cost[u] += 1
    v_cost[v] += 1

e_cost = [0 for i in range(N)]


def dfs(v):
    e_cost[v] += v_cost[v]
    for nv in tree[v]:
        dfs(nv)
        e_cost[v] += e_cost[nv]


dfs(0)

for i in range(N):
    edge_cost[i] += e_cost[i]

# print(edge_cost)


class LCA:
    def __init__(self, n, graph, edge_cost, root=0):
        """
        n     : 頂点数
        graph : 隣接リスト
        edge_cost: 辺のコスト (edge_cost[i]: iとiの親の頂点間の辺のコスト)
        root  : 根にする頂点
        """

        self.n = n
        self.graph = graph
        self.root = root
        self.edge_cost = edge_cost

        # LOG = 2^k <= n を満たす最大の k に少し余裕を持たせたもの
        self.LOG = max(1, (n - 1).bit_length())

        # parent[k][v] := 頂点 v の 2^k 個上の祖先
        self.parent = [[-1] * n for _ in range(self.LOG)]

        # min_cost[k][v] := 頂点 v ~ 2^k 個上の祖先の pathに含まれる辺のmin cost
        self.min_cost = [[float("inf")] * n for _ in range(self.LOG)]

        # depth[v] := 根からの深さ
        self.depth = [-1] * n

        # 根から BFS/DFS して、
        # parent[0][v]（1個上の親）と depth[v] を埋める
        self._build()

        # ダブリングテーブル構築
        self._doubling()

    def _build(self):
        """parent[0], depth を BFS で構築"""
        q = deque([self.root])
        self.depth[self.root] = 0
        self.parent[0][self.root] = -1
        self.min_cost[0][self.root] = float("inf")

        while q:
            v = q.popleft()
            for nv in self.graph[v]:
                if self.depth[nv] != -1:
                    continue
                self.depth[nv] = self.depth[v] + 1
                self.parent[0][nv] = v
                self.min_cost[0][nv] = edge_cost[nv]
                q.append(nv)

    def _doubling(self):
        """parent[k][v] を構築"""
        for k in range(self.LOG - 1):
            for v in range(self.n):
                p = self.parent[k][v]
                if p == -1:
                    self.parent[k + 1][v] = -1
                    self.min_cost[k + 1][v] = float("inf")
                else:
                    self.parent[k + 1][v] = self.parent[k][p]
                    self.min_cost[k + 1][v] = min(
                        self.min_cost[k][v], self.min_cost[k][p]
                    )

    def kth_ancestor(self, v, k):
        """
        頂点 v の k 個上の祖先を返す
        存在しなければ -1
        """
        for i in range(self.LOG):
            if k >> i & 1:
                v = self.parent[i][v]
                if v == -1:
                    return -1
        return v

    def lca(self, u, v):
        """u, v の最近共通祖先を返す"""

        # 深さを揃える
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        u = self.kth_ancestor(u, diff)

        # 揃えた時点で一致したら、それが LCA
        if u == v:
            return u

        # 大きい方の 2^k から順に、
        # まだ一致しないなら両方まとめて上げる
        for k in range(self.LOG - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]

        # 1個上が LCA
        return self.parent[0][u]

    def dist(self, u, v):
        """u, v 間の距離（辺数）"""
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]

    def _get_min_cost(self, u, v):
        """
        u~vのpathに含まれる辺のコストの最小値
        u, vのlcaの頂点がu
        """
        dist_uv = self.dist(u, v)
        now = v
        res = float("inf")
        for k in range(self.LOG):
            if dist_uv >> k & 1:
                res = min(res, self.min_cost[k][now])
                now = self.parent[k][now]
        return res

    def get_min_cost(self, u, v):
        """u~vのpathに含まれる辺のコストの最小値"""
        uv_lca = lca.lca(u, v)
        if u == v:
            return 0
        if uv_lca == u:
            return self._get_min_cost(u, v)
        elif uv_lca == v:
            return self._get_min_cost(v, u)
        else:
            return min(self._get_min_cost(uv_lca, u), self._get_min_cost(uv_lca, v))

    def is_ancestor(self, u, v):
        """
        u が v の祖先かどうか
        （u == v も True）
        """
        return self.lca(u, v) == u


lca = LCA(N, tree, edge_cost)
# print(lca.min_cost)
# print(lca._get_min_cost(0, 3))
R = int(input())

for _ in range(R):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(lca.get_min_cost(a, b))
