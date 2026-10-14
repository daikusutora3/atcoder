import sys

sys.setrecursionlimit(10**6)


# https://algo-method.com/descriptions/136
class UnionFind:
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x  # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x])  # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False  # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]:  # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx  # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]:  # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]  # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


N = int(input())
A = [list(map(int, input().split())) for i in range(N - 1)]
ans = True

aij = []
for i in range(N - 1):
    # (距離, i, j)
    aij += [(a, i, j + i + 1) for j, a in enumerate(A[i])]

aij.sort()
uf = UnionFind(N)
graph = [[] for i in range(N)]
for a, i, j in aij:
    if uf.size(0) == N:
        break
    if not uf.issame(i, j):
        graph[i].append((j, a))
        graph[j].append((i, a))
    uf.unite(i, j)


def dfs(v, p, dist, root):
    global A
    if root < v:
        if A[root][v - root - 1] != dist:
            return False
    res = True
    for u, w in graph[v]:
        if u == p:
            continue
        res = res and dfs(u, v, dist + w, root)
    return res


check = True
for i in range(N - 1):
    check = check and dfs(i, -1, 0, i)

print("Yes" if check else "No")
