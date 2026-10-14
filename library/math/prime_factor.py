def sieve_primes(n):
    """n 以下の素数リストを返す。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.md
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]


def factorize_by_primes(n, primes):
    """素数リスト primes を使って n を素因数分解し、[(p, e), ...] を返す。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.md
    """
    res = []

    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            res.append((p, e))

    if n > 1:
        res.append((n, 1))

    return res


def build_spf(n):
    """0..n の最小素因数テーブルを返す。spf[x] は x の最小素因数。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.md
    """
    spf = [0] * (n + 1)
    if n >= 1:
        spf[1] = 1

    for i in range(2, n + 1):
        if spf[i] != 0:
            continue

        spf[i] = i
        if i * i > n:
            continue

        for j in range(i * i, n + 1, i):
            if spf[j] == 0:
                spf[j] = i

    return spf


def build_linear_spf(n):
    """線形篩で (spf, primes) を返す。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.md
    """
    spf = [0] * (n + 1)
    primes = []

    if n >= 1:
        spf[1] = 1

    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)

        for p in primes:
            v = i * p
            if v > n or p > spf[i]:
                break
            spf[v] = p

    return spf, primes


def factorize_spf(n, spf):
    """spf テーブルを使って n を素因数分解し、[(p, e), ...] を返す。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.md
    """
    res = []

    while n > 1:
        p = spf[n]
        e = 0
        while n > 1 and spf[n] == p:
            n //= p
            e += 1
        res.append((p, e))

    return res


def divisors_from_factorization(factors):
    """[(p, e), ...] から約数を昇順で返す。

    Source: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.py
    Docs: https://github.com/daikusutora3/atcoder/blob/cdc3259e403ef68728af57ea4b6d54c34540eb35/library/math/prime_factor.md
    """
    divs = [1]

    for p, e in factors:
        cur = []
        mul = 1
        for _ in range(e + 1):
            for d in divs:
                cur.append(d * mul)
            mul *= p
        divs = cur

    divs.sort()
    return divs
