import sys

sys.setrecursionlimit(10**6)


class PersistentArray:
    """
    永続配列

    root = pa.root

    root = pa.set(root, i, x)
    root = pa.set_range(root, l, r, x)

    pa.get(root, i)
    pa.sum(root, l, r)

    計算量:
        build     : O(N)
        get       : O(log N)
        sum       : O(log N)
        set       : O(log N)
        set_range : O(log N)

    メモリ:
        build : O(N)
        更新1回につき O(log N)
    """

    def __init__(self, A):
        self.n = len(A)

        self.left = []
        self.right = []
        self.lazy = []
        self.sum_ = []

        self.root = self._build(A, 0, self.n)

    def _new(self, left=-1, right=-1, lazy=None, sum_=0):
        v = len(self.sum_)

        self.left.append(left)
        self.right.append(right)
        self.lazy.append(lazy)
        self.sum_.append(sum_)

        return v

    def _copy(self, v):
        return self._new(
            self.left[v],
            self.right[v],
            self.lazy[v],
            self.sum_[v],
        )

    def _build(self, A, l, r):
        if r - l == 1:
            return self._new(lazy=A[l], sum_=A[l])

        m = (l + r) // 2

        left = self._build(A, l, m)
        right = self._build(A, m, r)

        return self._new(
            left,
            right,
            sum_=self.sum_[left] + self.sum_[right],
        )

    def _push(self, v, l, r):
        if self.lazy[v] is None:
            return

        x = self.lazy[v]
        m = (l + r) // 2

        left = self._copy(self.left[v])
        right = self._copy(self.right[v])

        self.lazy[left] = x
        self.lazy[right] = x

        self.sum_[left] = x * (m - l)
        self.sum_[right] = x * (r - m)

        self.left[v] = left
        self.right[v] = right
        self.lazy[v] = None

    def get(self, root, i):
        l, r = 0, self.n
        v = root

        while r - l > 1:
            if self.lazy[v] is not None:
                return self.lazy[v]

            m = (l + r) // 2

            if i < m:
                v = self.left[v]
                r = m
            else:
                v = self.right[v]
                l = m

        return self.sum_[v]

    def sum(self, root, ql, qr):
        """[ql, qr) の和"""

        def dfs(v, l, r):
            if qr <= l or r <= ql:
                return 0

            if ql <= l and r <= qr:
                return self.sum_[v]

            if self.lazy[v] is not None:
                overlap = min(r, qr) - max(l, ql)
                return self.lazy[v] * overlap

            m = (l + r) // 2

            return dfs(self.left[v], l, m) + dfs(self.right[v], m, r)

        return dfs(root, 0, self.n)

    def set_range(self, root, ql, qr, x):
        """[ql, qr) をすべて x にした新しい root を返す"""

        def dfs(v, l, r):
            if qr <= l or r <= ql:
                return v

            nv = self._copy(v)

            if ql <= l and r <= qr:
                self.lazy[nv] = x
                self.sum_[nv] = x * (r - l)
                return nv

            self._push(nv, l, r)

            m = (l + r) // 2

            self.left[nv] = dfs(self.left[nv], l, m)
            self.right[nv] = dfs(self.right[nv], m, r)

            self.sum_[nv] = self.sum_[self.left[nv]] + self.sum_[self.right[nv]]

            return nv

        return dfs(root, 0, self.n)

    def set(self, root, i, x):
        return self.set_range(root, i, i + 1, x)

    def debug(self, root):
        """
        root が表す配列を list として復元して表示する。

        計算量: O(N)
        """
        A = [0] * self.n

        def dfs(v, l, r):
            # この区間が全部同じ値
            if self.lazy[v] is not None:
                A[l:r] = [self.lazy[v]] * (r - l)
                return

            # 葉
            if r - l == 1:
                A[l] = self.sum_[v]
                return

            m = (l + r) // 2

            dfs(self.left[v], l, m)
            dfs(self.right[v], m, r)

        dfs(root, 0, self.n)

        print(A)
        return A


Q, D = map(int, input().split())
INF = float("inf")
a = [INF for i in range(Q + 1)]
a[0] = 0
pa = PersistentArray(a)
stack = [pa.root]

rui = [i * D for i in range(Q + 1)]
for i in range(Q):
    rui[i + 1] += rui[i]


def bisect_left(root, x):
    global pa
    l, r = 0, pa.n
    while l < r:
        m = (l + r) // 2

        if pa.get(root, m) < x:
            l = m + 1
        else:
            r = m
    return l


for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, x = map(int, query.split())
        x = x + (len(stack) - 1) * D
        # print("add: ", x)
        t = pa.get(stack[-1], len(stack) - 1)
        if t <= x <= t + 2 * D or len(stack) == 1:
            root = pa.set(stack[-1], len(stack), x)
            stack.append(root)
        elif x > t + 2 * D:
            x = t + 2 * D
            root = pa.set(stack[-1], len(stack), x)
            stack.append(root)
        else:
            root = pa.set_range(stack[-1], bisect_left(stack[-1], x), len(stack) + 1, x)
            stack.append(root)
    elif query[0] == "2":
        stack.pop()
        # print("pop")
    else:
        ans = 0
        ans += pa.sum(stack[-1], 0, len(stack))
        print(ans - rui[max(0, len(stack) - 2)])

    # pa.debug(stack[-1])
