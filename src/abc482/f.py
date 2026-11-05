import sys
from collections import deque


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


N, M = list(map(int, input().split()))

if N == 1:
    for i in range(M):
        print(1 if i == 1 % M else -1)
    sys.exit()

primes = sieve_primes(int(N**0.5) + 1)
factors = factorize_by_primes(N, primes)
INF = float("inf")
D = len(factors)


def id(i, r):
    return i * M + r


dist = [INF for i in range(D * M)]
dist[id(0, 1 % M)] = 0

queue = deque([(0, 1 % M)])

while queue:
    i, r = queue.popleft()
    v = id(i, r)
    p, e = factors[i]
    for a in range(e + 1):
        w = 1 if i == 0 else 0
        ni, nr = (i + 1) % D, (r * pow(p, a, mod=M) % M)
        nv = id(ni, nr)
        if dist[nv] > dist[v] + w:
            dist[nv] = dist[v] + w
            if w == 0:
                queue.appendleft((ni, nr))
            else:
                queue.append((ni, nr))

for d in dist[:M]:
    if d == INF:
        print(-1)
    elif d == 0:
        print(1)
    else:
        print(d)
