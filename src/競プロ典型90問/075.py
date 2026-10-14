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


N = int(input())
primes = sieve_primes(int(N**0.5) + 1)
factors = factorize_by_primes(N, primes)
cnt = sum([a[1] for a in factors])
ans = 0
while cnt > 1:
    cnt = cnt // 2 + (1 if cnt % 2 == 1 else 0)
    ans += 1

print(ans)
