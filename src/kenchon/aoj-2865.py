from heapq import heapify, heappop, heappush


class DualSlopeTrick:
    """
    Dual Slope Trick

    凸関数 f(x) の凸共役 f*(x) を通常の Slope Trick として管理する。

    管理しているもの:
        min_f : f* の最小値
        L     : f* の左側の breakpoint
        R     : f* の右側の breakpoint

    そして

        f(0) = -min_f

    である。

    参考:
        https://maspypy.com/slope-trick-3-slope-trick-%E3%81%AE%E5%87%B8%E5%85%B1%E5%BD%B9

    主な操作:

        get_at_zero()
        add_all(a)
        add_linear(a, b)
        add_x_minus_a(a)
        add_a_minus_x(a)
        add_abs(a)
        shift(a)
        min_plus_convolve(other)
    """

    def __init__(self, INF=float("inf")):
        """
        計算量: O(1)

        初期状態:

            f(0) = 0
            f(x) = INF (x != 0)

        """

        self.INF = INF

        # f* の最小値
        self.min_f = 0

        # L: 最大値を O(1) で取りたいので -1 倍して min heap に入れる
        self.L = []

        # R: 最小値を O(1) で取りたい
        self.R = []

        # lazy
        self.add_L = 0
        self.add_R = 0

    # ============================================================
    # L
    # ============================================================

    def _top_L(self):
        """
        計算量: O(1)

        L の最大値を返す。
        """

        if not self.L:
            return -self.INF

        return -self.L[0] + self.add_L

    def _pop_L(self):
        """
        計算量: O(log N)

        L の最大値を取り出す。
        """

        if not self.L:
            return -self.INF

        return -heappop(self.L) + self.add_L

    def _push_L(self, x):
        """
        計算量: O(log N)

        L に x を追加する。
        """

        heappush(self.L, -(x - self.add_L))

    # ============================================================
    # R
    # ============================================================

    def _top_R(self):
        """
        計算量: O(1)

        R の最小値を返す。
        """

        if not self.R:
            return self.INF

        return self.R[0] + self.add_R

    def _pop_R(self):
        """
        計算量: O(log N)

        R の最小値を取り出す。
        """

        if not self.R:
            return self.INF

        return heappop(self.R) + self.add_R

    def _push_R(self, x):
        """
        計算量: O(log N)

        R に x を追加する。
        """

        heappush(self.R, x - self.add_R)

    # ============================================================
    # 基本操作
    # ============================================================

    def get_at_zero(self):
        """
        計算量: O(1)

        f(0) を返す。

        f*(p) = sup_x(px - f(x))

        より、

            min f* = -f(0)

        """

        return -self.min_f

    def add_all(self, a):
        """
        計算量: O(1)

        f(x) <- f(x) + a
        """

        # (f + a)* = f* - a
        self.min_f -= a

    # ============================================================
    # 線形関数
    # ============================================================

    def add_linear(self, a, b=0):
        """
        計算量: O(1)

        f(x) <- f(x) + ax + b

        凸共役を取ると

            (f(x) + ax + b)*
            = f*(p-a) - b

        となる。
        """

        # breakpoint を全て a だけ右にずらす
        self.add_L += a
        self.add_R += a

        # f* の最小値を -b
        self.min_f -= b

    # ============================================================
    # shift
    # ============================================================

    def shift(self, d):
        """
        計算量: O(|d| log N)

        f(x) <- f(x-d)

        d > 0:
            f(x-d)
            = f を右に d 移動

        d < 0:
            f(x-d)
            = f を左に -d 移動

        1 回の shift は、

            d > 0:
                L の最大値を R に移す

            d < 0:
                R の最小値を L に移す

        ことで実現できる。
        """

        if d > 0:
            for _ in range(d):
                x = self._pop_L()

                # f*(p) に +p を加える
                # 最小値が x だけ増える
                self.min_f += x

                self._push_R(x)

        elif d < 0:
            for _ in range(-d):
                x = self._pop_R()

                # f*(p) に -p を加える
                self.min_f -= x

                self._push_L(x)

    # ============================================================
    # (x-a)_+
    # ============================================================

    def add_x_minus_a(self, a):
        """
        計算量: O(|a| log N)

        f(x) <- f(x) + (x-a)_+

        """

        # x -> x+a として原点へ持ってくる
        self.shift(-a)

        # x_+ を加える
        #
        # 凸共役側では右側の breakpoint が
        # 追加されるのではなく、
        # R 全体の傾きが +1 増える。
        self.add_R += 1

        # 元の座標へ戻す
        self.shift(a)

    # ============================================================
    # (a-x)_+
    # ============================================================

    def add_a_minus_x(self, a):
        """
        計算量: O(|a| log N)

        f(x) <- f(x) + (a-x)_+

        """

        self.shift(-a)

        # (-x)_+ を加える
        #
        # 左側の slope が -1 増える。
        self.add_L -= 1

        self.shift(a)

    # ============================================================
    # |x-a|
    # ============================================================

    def add_abs(self, a):
        """
        計算量: O(|a| log N)

        f(x) <- f(x) + |x-a|

        |x-a|
            = (x-a)_+ + (a-x)_+
        """

        self.add_x_minus_a(a)
        self.add_a_minus_x(a)

    # ============================================================
    # min-plus convolution
    # ============================================================

    def min_plus_convolve(self, other):
        """
        計算量: O(M log(N+M))

        f <- f □ g

        ただし

            (f □ g)(x)
              = min_y f(y) + g(x-y)

        とする。

        凸共役を取ると

            (f □ g)* = f* + g*

        なので、内部の通常の Slope Trick の
        breakpoint をマージすればよい。

        other は破壊しない。
        """

        self.min_f += other.min_f

        # other の L をそのまま足す
        for x in other.L:
            x = -x + other.add_L
            self._push_L(x)

        # other の R をそのまま足す
        for x in other.R:
            x = x + other.add_R
            self._push_R(x)

        return self

    # ============================================================
    # おまけ
    # ============================================================

    def clear_right(self):
        """
        計算量: O(1)

        凸共役側で右側の slope を全て捨てる。
        """

        self.R = []
        self.add_R = 0

    def clear_left(self):
        """
        計算量: O(1)

        凸共役側で左側の slope を全て捨てる。
        """

        self.L = []
        self.add_L = 0


N = int(input())
d = list(map(int, input().split())) + [10**18]
g = list(map(int, input().split()))

DST = DualSlopeTrick()

for i in range(N):
    DST2 = DualSlopeTrick()
    DST2._push_L(-g[i])
    DST2._push_R(-g[i])
    DST.min_plus_convolve(DST2)
    DST.add_abs(d[i])
    DST.add_all(g[i])


print(DST.get_at_zero())
