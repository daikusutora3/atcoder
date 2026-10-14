R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())

MOD = 10**9 + 7

MAX = 901

fact = [1] * (MAX + 1)
invfact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD


def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD


# X✖️Yにおけるサーバーとデスクの組み合わせ
ans = 0
for bit in range(16):
    h, w = X, Y
    for i in range(4):
        if bit >> i & 1:
            if i % 2 == 0:
                h -= 1
            else:
                w -= 1
    if h <= 0 or w <= 0:
        continue
    if bit.bit_count() % 2 == 0:
        ans += comb(h * w, D) * comb(h * w - D, L)
    else:
        ans -= comb(h * w, D) * comb(h * w - D, L)
    ans %= MOD


ans *= (R - X + 1) * (C - Y + 1)
ans %= MOD

print(ans)
