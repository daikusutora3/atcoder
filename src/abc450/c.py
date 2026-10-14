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
grid = [input() for i in range(H)]
uf = UnionFind(H * W + 2)
for i in range(H):
    for j in range(W):
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni = i + di
            nj = j + dj
            if grid[i][j] == ".":
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    uf.unite(i + j * H, H * W)
                elif grid[ni][nj] == ".":
                    uf.unite(i + j * H, ni + nj * H)

seen = set()
for i in range(H):
    for j in range(W):
        r = uf.root(i + j * H)
        if grid[i][j] == "." and (not uf.issame(H * W, i + j * H)):
            seen.add(uf.root(i + j * H))

print(len(seen))
