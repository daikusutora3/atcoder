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


N, M = map(int, input().split())
UV = [list(map(int, input().split())) for i in range(M)]
UV = [[uv[0] - 1, uv[1] - 1] for uv in UV]


# １番目: ２分探索
def is_ok(k):
    global N, M, UV
    uf = UnionFind(N)
    for u, v in UV[k:]:
        uf.unite(u, v)
    seen = set()
    for i in range(N):
        root = uf.root(i)
        seen.add(root)
    return len(seen) >= 2


mod = 998244353
ok = M + 1
ng = 0

while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid


# 2番目: ２^(i+1)の辺のコストの総和を求める
ans = 0

for i in range(ok):
    ans += pow(2, i + 1, mod)
    ans %= mod

# 3番目: 消しすぎた辺を戻していく
uf = UnionFind(N)
for u, v in UV[ok:]:
    uf.unite(u, v)

seen = set()
for i in range(N):
    root = uf.root(i)
    seen.add(root)

for i, uv in enumerate(UV[:ok]):
    u, v = uv
    root_u = uf.root(u)
    root_v = uf.root(v)
    if root_u == root_v:
        ans = ans + mod - pow(2, i + 1, mod)
        ans %= mod

print(ans)
