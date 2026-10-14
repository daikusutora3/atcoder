def comb_small_k(n, k, mod):
    """素数 mod で、min(k, n-k) 回の積から nCk を求める。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/mod_comb.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/mod_comb.md
    """
    if mod <= 1:
        raise ValueError("mod must be greater than 1")
    if n < 0 or k < 0 or k > n:
        return 0

    k = min(k, n - k)
    if k >= mod:
        raise ValueError("min(k, n-k) must be smaller than mod")

    num = 1
    den = 1
    for i in range(1, k + 1):
        num = num * (n - k + i) % mod
        den = den * i % mod

    return num * pow(den, mod - 2, mod) % mod


def pascal_row(n, mod):
    """Pascal の漸化式で [nC0, nC1, ..., nCn] mod mod を返す。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/mod_comb.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/mod_comb.md
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if mod <= 0:
        raise ValueError("mod must be positive")

    row = [0] * (n + 1)
    row[0] = 1 % mod

    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            row[j] = (row[j] + row[j - 1]) % mod

    return row


class ModComb:
    """素数 mod における階乗・順列・二項係数を前計算する。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/mod_comb.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/mod_comb.md
    """

    def __init__(self, max_n, mod):
        if max_n < 0:
            raise ValueError("max_n must be non-negative")
        if mod <= 1:
            raise ValueError("mod must be greater than 1")
        if max_n >= mod:
            raise ValueError("max_n must be smaller than mod")

        self.max_n = max_n
        self.mod = mod

        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % mod

        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
        for i in range(max_n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % mod

        self.fact = fact
        self.inv_fact = inv_fact

    def comb(self, n, k):
        """nCk mod mod を返す。k が範囲外なら 0。
        """
        if n < 0:
            return 0
        if n > self.max_n:
            raise ValueError("n exceeds max_n")
        if k < 0 or k > n:
            return 0
        return (
            self.fact[n] * self.inv_fact[k] % self.mod * self.inv_fact[n - k] % self.mod
        )

    def perm(self, n, k):
        """nPk mod mod を返す。k が範囲外なら 0。
        """
        if n < 0:
            return 0
        if n > self.max_n:
            raise ValueError("n exceeds max_n")
        if k < 0 or k > n:
            return 0
        return self.fact[n] * self.inv_fact[n - k] % self.mod
