class CumulativeSum2D:
    """2次元累積和。sum(x1, y1, x2, y2) で半開区間の和を返す。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/misc/prefix_sum_2d.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/misc/prefix_sum_2d.md
    """

    def __init__(self, a):
        self.h = h = len(a)
        self.w = w = len(a[0]) if h else 0
        if any(len(row) != w for row in a):
            raise ValueError("all rows must have the same length")
        self.s = s = [[0] * (w + 1) for _ in range(h + 1)]
        for y, row in enumerate(a):
            prev, cur = s[y], s[y + 1]
            total = 0
            for x, v in enumerate(row):
                total += v
                cur[x + 1] = prev[x + 1] + total

    def sum(self, x1, y1, x2, y2):
        """[y1, y2) 行 × [x1, x2) 列の和。右下の境界は含まない。
        """
        if not (0 <= y1 <= y2 <= self.h and 0 <= x1 <= x2 <= self.w):
            raise ValueError("rectangle must satisfy 0 <= start <= end <= size")
        s = self.s
        return s[y2][x2] - s[y1][x2] - s[y2][x1] + s[y1][x1]
