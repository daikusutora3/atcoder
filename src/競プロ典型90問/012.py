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


H, W = map(int, input().split())
grid = ["white" for i in range(H * W)]
Q = int(input())

uf = UnionFind(H * W)

ans = []
for _ in range(Q):
    query = input()
    if query[0] == "1":
        r, c = map(int, query[2:].split())
        r, c = r - 1, c - 1
        grid[r + c * H] = "red"
        # 上下左右を確認してunionする
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W:
                if grid[nr + nc * H] == "red":
                    uf.unite(r + c * H, nr + nc * H)
    if query[0] == "2":
        ra, ca, rb, cb = map(int, query[2:].split())
        ra, ca, rb, cb = ra - 1, ca - 1, rb - 1, cb - 1
        if ra == rb and ca == cb:
            ans.append("Yes" if grid[ra + ca * H] == "red" else "No")
        elif uf.issame(ra + ca * H, rb + cb * H):
            ans.append("Yes")
        else:
            ans.append("No")

print(*ans, sep="\n")
