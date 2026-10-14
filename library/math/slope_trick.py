from heapq import heapify, heappop, heappush


class SlopeTrick:
    """
    以下の記事を下に実装しています。
    https://maspypy.com/slope-trick-1-%E8%A7%A3%E8%AA%AC%E7%B7%A8
    """

    def __init__(self, min_f, L, R, INF=float("inf")):
        """
        計算量: O(N)

        min_f: 区分線形凸関数における最小値
        L: 降順に取り出すためのheapque、全ての値が-1倍されている
        R: 昇順に取り出すためのheapque
        add_L: Lに対して一斉に加算される値
        add_R: Rに対して一斉に加算される値
        """
        self.INF = INF
        self.min_f = min_f
        self.L = [-l for l in L[:]]
        self.R = R[:]
        self.add_L = 0
        self.add_R = 0
        heapify(self.L)
        heapify(self.R)

    def _top_R(self):
        if len(self.R) == 0:
            return self.INF
        return self.R[0] + self.add_R

    def _pop_R(self):
        if len(self.R) == 0:
            return self.INF
        return heappop(self.R) + self.add_R

    def _push_R(self, x):
        return heappush(self.R, x - self.add_R)

    def _top_L(self):
        if len(self.L) == 0:
            return -self.INF
        return -self.L[0] + self.add_L

    def _pop_L(self):
        if len(self.L) == 0:
            return -self.INF
        return -heappop(self.L) + self.add_L

    def _push_L(self, x):
        return heappush(self.L, -(x - self.add_L))

    def get_min(self):
        """
        計算量: O(1)
        区分線形凸関数における最小値
        """
        return self.min_f

    def add_all(self, a):
        """
        計算量: O(1)
        区分線形凸関数全体にaを加算する
        """
        self.min_f += a

    def add_x_minus_a(self, a):
        """
        計算量: O(logN)
        区分線形凸関数に(x-a)_{+}を加算する
        """
        self.min_f += max(0, self._top_L() - a)
        self._push_L(a)
        self._push_R(self._pop_L())

    def add_a_minus_x(self, a):
        """
        計算量: O(logN)
        区分線形凸関数に(a-x)_{+}を加算する
        """
        self.min_f += max(0, a - self._top_R())
        self._push_R(a)
        self._push_L(self._pop_R())

    def add_abs(self, a):
        """
        計算量: O(logN)
        区分線形凸関数に|x-a|を加算する
        """
        self.add_a_minus_x(a)
        self.add_x_minus_a(a)

    def clear_right(self):
        """
        計算量: O(1)
        区分線形凸関数に対して累積minを取る
        """
        self.R = []
        self.add_R = 0

    def clear_left(self):
        """
        計算量: O(1)
        区分線形凸関数に対して右側累積minを取る
        """
        self.L = []
        self.add_L = 0

    def shift(self, add_L, add_R):
        """
        計算量: O(1)
        sliding window minimum をとる操作
        """
        if not (add_L <= add_R):
            raise ValueError("must be add_L <= add_R")
        self.add_L += add_L
        self.add_R += add_R

    def get(self, x):
        """
        計算量: O(len(L) + len(R))
        区分線形凸関数f(x)の値を求める
        """
        res = self.min_f
        L = self.L[:]
        R = self.R[:]
        while len(L):
            # (a-x)_{+}の値
            res += max(0, -heappop(L) + self.add_L - x)
        while len(R):
            # (x-a)_{+}の値
            res += max(0, x - (heappop(R) + self.add_R))
        return res
