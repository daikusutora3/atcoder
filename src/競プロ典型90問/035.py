from collections import deque


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
        self.LOG = (n - 1).bit_length()

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

    def dist(self, u, v):
        """u, v 間の距離（辺数）"""
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]

    def is_ancestor(self, u, v):
        """
        u が v の祖先かどうか
        （u == v も True）
        """
        return self.lca(u, v) == u


N = int(input())
graph = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

lca = LCA(N, graph, root=0)

memo = []


def dfs(v, p):
    global memo
    memo.append(v)
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v)


dfs_order = [-1 for i in range(N)]
dfs(0, -1)
for i in range(N):
    dfs_order[memo[i]] = i


def solve():
    query = list(map(int, input().split()))
    V = query[1:]
    V.sort(key=lambda x: dfs_order[x])

    ans = 0
    k = len(V)
    for i in range(k):
        ans += lca.dist(V[i], V[(i + 1) % k])

    return ans // 2


Q = int(input())
for _ in range(Q):
    print(solve())
