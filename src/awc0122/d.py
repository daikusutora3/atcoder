class SparseTable:
    """
    Sparse Table（静的区間クエリ）

    使用方法:
        st = SparseTable(op, e, v)

        st.get(p)        # v[p]
        st.prod(l, r)    # 区間 [l, r) の演算結果
        st.all_prod()    # 配列全体の演算結果
        len(st)          # 配列の長さ

    制約:
        op は結合法則と冪等性を満たす必要がある。

        冪等性:
            op(x, x) == x

        使用可能な例:
            min
            max
            gcd
            bitwise AND
            bitwise OR

        通常の加算・乗算には使用できない。

    計算量:
        構築       : O(N log N)
        get        : O(1)
        prod       : O(1)
        all_prod   : O(1)
        メモリ     : O(N log N)
    """

    def __init__(self, op, e, v):
        """
        op : 二項演算
        e  : 単位元
        v  : 元となる配列
        """

        self._op = op
        self._e = e
        self._n = len(v)

        # log[i] := floor(log2(i))
        self._log = [0] * (self._n + 1)

        for i in range(2, self._n + 1):
            self._log[i] = self._log[i >> 1] + 1

        if self._n == 0:
            self._data = []
            return

        # data[k][i]
        # := 区間 [i, i + 2^k) の演算結果
        height = self._log[self._n] + 1
        self._data = [list(v)]

        for k in range(1, height):
            length = 1 << k
            half = length >> 1

            previous = self._data[k - 1]
            row_length = self._n - length + 1
            row = [e] * row_length

            for i in range(row_length):
                row[i] = op(
                    previous[i],
                    previous[i + half],
                )

            self._data.append(row)

    def __len__(self):
        """
        配列の長さを返す。

        計算量: O(1)
        """
        return self._n

    def get(self, p):
        """
        v[p] を返す。

        計算量: O(1)
        """
        assert 0 <= p < self._n

        return self._data[0][p]

    def prod(self, l, r):
        """
        区間 [l, r) の演算結果を返す。

        l == r の場合は単位元 e を返す。

        計算量: O(1)
        """
        assert 0 <= l <= r <= self._n

        if l == r:
            return self._e

        length = r - l
        k = self._log[length]
        width = 1 << k

        # [l, l + 2^k)
        # [r - 2^k, r)
        #
        # この2区間で [l, r) を覆う。
        # 区間が重なっても、op が冪等なら問題ない。
        return self._op(
            self._data[k][l],
            self._data[k][r - width],
        )

    def all_prod(self):
        """
        配列全体 [0, N) の演算結果を返す。

        計算量: O(1)
        """
        return self.prod(0, self._n)


N, Q = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]
ST_LIST = [SparseTable(max, -float("inf"), a) for a in A]


def f(v):
    L = list(str(v))
    res = sum([int(l) for l in L])
    L[0] = int(L[0]) - 1
    for i in range(1, len(L)):
        L[i] = 9
    res = max(res, sum(L))
    return res


for _ in range(Q):
    L, P, T = map(int, input().split())
    L -= 1
    P -= 1
    if P > L:
        print("NA")
        continue
    V = -float("inf")
    for i in range(L, min(N, L + T + 1)):
        V = max(V, ST_LIST[i].prod(P, P + i - L + 1))
    print(f(V))
