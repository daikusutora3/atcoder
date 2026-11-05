def sieve_primes(n):
    """n 以下の素数リストを返す。

    計算量: 時間 O(n log log n)、空間 O(n)。

    Source: https://github.com/daikusutora3/atcoder
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

    計算量: 時間 O(P + log n)、出力空間 O(r)。P は試す素数数、r は異なる素因数数。

    Source: https://github.com/daikusutora3/atcoder
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


N, M = map(int, input().split())

primes = sieve_primes(int(N**0.5) + 1)
factors = factorize_by_primes(N, primes)
INF = float("inf")
dist = [INF for i in range(M)]
dist[1 % M] = 1

for p, e in factors:
    n_dist = [INF for i in range(M)]
    for k in range(M):
        i = k
        cnt = 0
        seen = {i}
        while n_dist[i] != INF:
            ni = (i * p) % M
            if ni in seen:
                break
            seen.add(ni)
            n_dist[ni] = min(n_dist[ni], dist[ni], max(dist[k], 1 + cnt // e))
            cnt += 1
            i = ni
    dist = n_dist

for d in dist:
    print(-1 if d == INF else d)
