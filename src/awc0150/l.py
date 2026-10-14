import sys
from collections import deque

from sortedcontainers import SortedList

sys.setrecursionlimit(10**6)


import sys

sys.setrecursionlimit(10**6)


class CentroidDecomposition:
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph
        self.size = [0] * n
        self.used = [False] * n
        self.parent = [-1] * n
        self.children = [[] for _ in range(n)]
        self.members = [[] for _ in range(n)]

        self.root = self._build(0, -1)

    def _calc_size(self, v, p, members):
        self.size[v] = 1
        members.append(v)

        for nv in self.graph[v]:
            if nv == p or self.used[nv]:
                continue
            self._calc_size(nv, v, members)
            self.size[v] += self.size[nv]

    def _find_centroid(self, v, p, total):
        for nv in self.graph[v]:
            if nv == p or self.used[nv]:
                continue
            if self.size[nv] > total // 2:
                return self._find_centroid(nv, v, total)
        return v

    def _build(self, v, p):
        members = []
        self._calc_size(v, -1, members)

        c = self._find_centroid(v, -1, self.size[v])

        self.parent[c] = p
        self.members[c] = members
        self.used[c] = True

        for nv in self.graph[c]:
            if self.used[nv]:
                continue
            child = self._build(nv, c)
            self.children[c].append(child)

        return c

    def ancestors(self, v):
        res = []
        v = self.parent[v]

        while v != -1:
            res.append(v)
            v = self.parent[v]

        return res[::-1]

    def debug(self):
        print("root:", self.root)

        for v in range(self.n):
            print(
                f"{v}: parent={self.parent[v]}, "
                f"children={self.children[v]}, "
                f"members={self.members[v]}"
            )


class WeightedLCA:
    def __init__(self, n, graph, root=0):
        self.n = n
        self.LOG = n.bit_length()

        self.parent = [[-1] * n for _ in range(self.LOG)]
        self.depth = [-1] * n
        self.dist_root = [0] * n

        que = deque([root])
        self.depth[root] = 0

        while que:
            v = que.popleft()

            for nv, w in graph[v]:
                if self.depth[nv] != -1:
                    continue

                self.parent[0][nv] = v
                self.depth[nv] = self.depth[v] + 1
                self.dist_root[nv] = self.dist_root[v] + w
                que.append(nv)

        for k in range(self.LOG - 1):
            for v in range(n):
                p = self.parent[k][v]
                if p != -1:
                    self.parent[k + 1][v] = self.parent[k][p]

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]

        for k in range(self.LOG):
            if diff >> k & 1:
                u = self.parent[k][u]

        if u == v:
            return u

        for k in range(self.LOG - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]

        return self.parent[0][u]

    def dist(self, u, v):
        p = self.lca(u, v)
        return self.dist_root[u] + self.dist_root[v] - 2 * self.dist_root[p]


N, Q = map(int, input().split())

g = [[] for i in range(N)]
tree = [[] for i in range(N)]
for _ in range(N - 1):
    A, B, C = map(int, input().split())
    A, B = A - 1, B - 1
    g[A].append(B)
    g[B].append(A)
    tree[A].append((B, C))
    tree[B].append((A, C))

cd = CentroidDecomposition(N, g)
lca = WeightedLCA(N, tree)
INF = float("inf")

open = [False for i in range(N)]
open[0] = True

value = [SortedList([INF]) for i in range(N)]
value[0].add(0)

for v in cd.ancestors(0):
    value[v].add(lca.dist(0, v))

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, X = query
        X -= 1
        if open[X]:
            open[X] = False
            value[X].remove(0)
            for v in cd.ancestors(X):
                value[v].remove(lca.dist(X, v))
        else:
            open[X] = True
            value[X].add(0)
            for v in cd.ancestors(X):
                value[v].add(lca.dist(X, v))
    else:
        _, V, T = query
        V -= 1
        res = INF
        res = min(res, value[V][0])
        for v in cd.ancestors(V):
            res = min(res, value[v][0] + lca.dist(V, v))
        if res <= T:
            print("YES")
        else:
            print("NO")
