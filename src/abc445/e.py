from array import array


def build_spf(n: int):
    # spf[x] = smallest prime factor of x (x>=2), spf[0]=spf[1]=0
    spf = array("I", [0]) * (n + 1)
    primes = []
    for x in range(2, n + 1):
        if spf[x] == 0:
            spf[x] = x
            primes.append(x)
        sx = spf[x]
        for p in primes:
            y = p * x
            if y > n or p > sx:
                break
            spf[y] = p
    return spf


def factorize_spf(x: int, spf):
    # return dict prime->exp でも list でもOK（この問題はdict/listどっちも使える）
    res = []
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        res.append((p, e))
    return res
