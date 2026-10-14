import math


N, K = map(int, input().split())
mod = 10**9 + 7


# xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
def modinv(x):
    return pow(x, mod - 2, mod)


modinv_table = [-1] * (N + 1)
for i in range(1, N + 1):
    modinv_table[i] = modinv(i)


def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans


print(binomial_coefficients(N - K + 1, K))
