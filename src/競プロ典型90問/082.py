L, R = map(int, input().split())

mod = 10**9 + 7


def sig(l, r):
    return r * (r + 1) // 2 - (l - 1) * l // 2


def solve(k):
    res = 0

    for i in range(1, 20):
        if k < 10**i:
            res += sig(10 ** (i - 1), k) * i
            res %= mod
            break
        elif k >= 10**i:
            res += sig(10 ** (i - 1), 10**i - 1) * i
            res %= mod
    return res


print((solve(R) - solve(L - 1)) % mod)
