import sys
from math import ceil, floor


def sieve_primes(n):
    """n 以下の素数リストを返す。"""
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
    """素数リスト primes を使って n を素因数分解し、[(p, e), ...] を返す。"""
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
    """0..n の最小素因数テーブルを返す。spf[x] は x の最小素因数。"""
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
    """線形篩で (spf, primes) を返す。"""
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
    """spf テーブルを使って n を素因数分解し、[(p, e), ...] を返す。"""
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
    """[(p, e), ...] から約数を昇順で返す。"""
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


N = int(input())
A = list(map(int, input().split()))

spf, primes = build_linear_spf(N + 1)

ab = [[1, -A[i]] for i in range(N)]
ab = [[-1, -1]] + ab
for i in range(N, 0, -1):
    for d in divisors_from_factorization(factorize_spf(i, spf)):
        if i == d:
            continue
        ab[d][0] -= ab[i][0]
        ab[d][1] -= ab[i][1]

INF = float("inf")
l, r = max(A), INF
for a, b in ab[1:]:
    if a == 0:
        if b < 0:
            l = INF
            r = -INF
    elif a > 0:
        l = max(l, ceil(-b / a))
    else:
        r = min(r, floor(-b / a))

if not (l <= r) or r < 0:
    print(-1)
    sys.exit()


x = max(0, l)

ans = 0
for i in range(N - 1, -1, -1):
    if A[i] < x:
        ans += x - A[i]
        for d in divisors_from_factorization(factorize_spf(i + 1, spf)):
            A[d - 1] += x - A[i]

print(ans)
