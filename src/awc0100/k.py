from bisect import bisect_left


B = 300


class Block:
    def __init__(self, values):
        B = len(values)
        self.B = B
        self.lazy = 0
        avals = [0] * B
        cvals = [0] * B
        id_i = [-1] * B
        for i, (id, aval, cval) in enumerate(values):
            id_i[id % B] = i
            avals[i] = aval
            cvals[i] = cval
        self.id_i = id_i
        self.avals = avals
        self.cvals = cvals
        self.suffix_min = [float("inf")] * (B + 1)
        self.calc_suffix_min()

    def __repr__(self):
        return f"[{self.lazy}, {self.avals}, {self.suffix_min}]"

    def get_id_i(self, id):
        # 元々左からid番目にあったものの現在の平方分割のブロックにおけるindex
        return self.id_i[id % self.B]

    def calc_suffix_min(self):
        # Blockの中は駐車スペースの数でソートされているので、suffix_minを取ると便利
        suffix_min = [float("inf")] * (self.B + 1)
        for i in range(self.B - 1, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], self.avals[i])
        self.suffix_min = suffix_min

    def bisect_left_cvals(self, X):
        return bisect_left(self.cvals, X)


N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ruiA = [0 for i in range(N + 1)]
ruiC = [0 for i in range(N + 1)]

for i in range(N):
    ruiA[i + 1] = ruiA[i] + A[i]
    ruiC[i + 1] = ruiC[i] + C[i]

values = [[i, ruiA[i + K] - ruiA[i], ruiC[i + K] - ruiC[i]] for i in range(N - K + 1)]


values.sort(key=lambda x: (x[0] // B) * (N + 1) + x[2])
n_blocks = (N - K + 1 + B - 1) // B
# i番目のブロックのindexは[block_start[i], block_end[i])
block_start = [i * B for i in range(n_blocks)]
block_end = [min(N - K + 1, (i + 1) * B) for i in range(n_blocks)]
blocks = [Block(values[block_start[b] : block_end[b]]) for b in range(n_blocks)]


def update(X, Y):
    """
    X: 更新するもののindex(0-index)
    Y: 更新した後の値
    """
    global n_blocks, blocks, values, N, K, B
    diff = Y - A[X]
    A[X] = Y
    l = max(0, X - K + 1)
    r = min(N - K + 1, X + 1)
    # print(f"=={X + 1}, {Y}, {diff}==")
    # print(f"[{l}, {r})")
    while l < r:
        if l % B == 0 and l + B <= r:
            blocks[l // B].lazy += diff
            l += B
        else:
            block = blocks[l // B]
            i = block.get_id_i(l)
            block.avals[i] += diff
            l += 1
            if l == r or l % B == 0:
                block.calc_suffix_min()


def question(X):
    global blocks
    res = float("inf")
    for block in blocks:
        bl = block.bisect_left_cvals(X)
        res = min(res, block.suffix_min[bl] + block.lazy)
    return res


for _ in range(Q):
    T, X, Y = map(int, input().split())
    if T == 1:
        update(X - 1, Y)
    else:
        ans = question(X)
        if ans == float("inf"):
            print("IMPOSSIBLE")
        else:
            print(ans)
