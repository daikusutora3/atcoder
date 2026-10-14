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


T = int(input())
for _ in range(T):
    x = int(input())
    primes = [2, 3, 5, 7]
    factors = factorize_by_primes(x, primes)
    ans = True
    for fac in factors:
        if fac[0] >= 10:
            ans = False
    if ans:
        print("Yes")
    else:
        print("No")
