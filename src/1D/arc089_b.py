class CumulativeSum2D:
    """2次元累積和。sum(x1, y1, x2, y2) で半開区間の和を返す。"""

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
        """[y1, y2) 行 × [x1, x2) 列の和。右下の境界は含まない。"""
        if not (0 <= y1 <= y2 <= self.h and 0 <= x1 <= x2 <= self.w):
            raise ValueError("rectangle must satisfy 0 <= start <= end <= size")
        s = self.s
        return s[y2][x2] - s[y1][x2] - s[y2][x1] + s[y1][x1]


N, K = map(int, input().split())
INF = float("inf")
dp = [[-INF for y in range(K + 1)] for x in range(K + 1)]
init = 0
a = [[0 for i in range(2 * K)] for _ in range(2 * K)]
for _ in range(N):
    x, y, c = list(input().split())
    x, y = int(x), int(y)
    if c == "B":
        if (x % (2 * K) < K and y % (2 * K) < K) or (
            K <= x % (2 * K) < 2 * K and K <= y % (2 * K) < 2 * K
        ):
            init += 1
    else:
        if x % (2 * K) < K <= y % (2 * K) < 2 * K or (
            K <= x % (2 * K) < 2 * K and y % (2 * K) < K
        ):
            init += 1
    if c == "B":
        a[x % (2 * K)][y % (2 * K)] += 1
    else:
        a[(x + K) % (2 * K)][y % (2 * K)] += 1

cs = CumulativeSum2D(a)
ans = 0
for x in range(K + 1):
    for y in range(K + 1):
        res = 0
        res += cs.sum(x, y, x + K, y + K)
        res += cs.sum(x + K, y + K, 2 * K, 2 * K)
        res += cs.sum(0, 0, x, y)
        res += cs.sum(x + K, 0, 2 * K, y)
        res += cs.sum(0, y + K, x, 2 * K)
        ans = max(ans, res, N - res)

print(ans)
