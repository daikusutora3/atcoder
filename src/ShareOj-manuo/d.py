# https://algo-method.com/descriptions/136
from collections import deque

INF = float("inf")


class UnionFind:
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
        self.player = [INF] * n

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

        # プレイヤーの更新
        if self.siz[rx] == self.siz[ry]:
            self.player[rx] = min(self.player[rx], self.player[ry])
        elif self.siz[rx] < self.siz[ry]:
            self.player[rx] = self.player[ry]
        else:
            self.player[rx] = self.player[rx]

        self.siz[rx] += self.siz[ry]  # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


H, W = map(int, input().split())
grid = [input() for i in range(H)]
Q = int(input())
uf = UnionFind(H * W)


def id(i, j):
    return i + j * H


que = deque([])
visited = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if "1" <= grid[i][j] <= "9":
            que.append((i, j))
            visited[i][j] = 1
            uf.player[id(i, j)] = int(grid[i][j])

while que:
    i, j = que.popleft()
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < H and 0 <= nj < W) or grid[ni][nj] == "#":
            continue
        if not visited[ni][nj]:
            uf.unite(id(i, j), id(ni, nj))
            visited[ni][nj] = 1
            que.append((ni, nj))

ans = [0 for i in range(10)]
seen = set()
for i in range(H):
    for j in range(W):
        if not uf.root(id(i, j)) in seen:
            seen.add(uf.root(id(i, j)))
            p = uf.player[id(i, j)]
            print(p)
            if p == float("inf"):
                continue
            print("!!", p, uf.size(id(i, j)))
            ans[p] += uf.size(id(i, j))

print(ans)
