X = int(input())


# https://qiita.com/alumite14/items/6e2335dc9d852151f2ca
class SparseTable:
    __slots__ = ("fold_op", "table")

    def __init__(self, init_arr: list, fold_op) -> None:
        self.fold_op = fold_op
        n = len(init_arr)
        h = n.bit_length()
        self.table = [init_arr[:]]
        self.table.extend([0] * n for _ in range(h - 1))

        for i in range(1, h):
            ct, pt = self.table[i], self.table[i - 1]
            for j in range(n - (1 << i) + 1):
                ct[j] = fold_op(pt[j], pt[j + (1 << (i - 1))])

    def fold_range(self, l: int, r: int):
        """Fold to the range [l, r) for an idempotent operation."""
        level = (r - l).bit_length() - 1
        return self.fold_op(self.table[level][l], self.table[level][r - (1 << level)])


spt = SparseTable(A, max)
