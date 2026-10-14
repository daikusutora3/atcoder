from atcoder.convolution import convolution

R, G, B, K = map(int, input().split())
X, Y, Z = map(int, input().split())


MOD = 998244353


MAX = 200000

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


Rcomb = [0 for i in range(min(K + 1, R + 1))]
for r in range(max(0, K - Y), min(K + 1, R + 1)):
    Rcomb[r] = comb(R, r)

Gcomb = [0 for i in range(min(K + 1, G + 1))]
for g in range(max(0, K - Z), min(K + 1, G + 1)):
    Gcomb[g] = comb(G, g)

RGconv = convolution(MOD, Rcomb, Gcomb)

ans = 0
for rg in range(min(R + G + 1, X + 1)):
    b = K - rg
    if b < K - X:
        break
    ans += RGconv[rg] * comb(B, b)
    ans %= MOD

print(ans)

# ans = 0
# for r in range(min(K + 1, R + 1)):
#     for g in range(min(K - r + 1, G + 1)):
#         if r + g > K or K - r - g > B:
#             continue
#         b = K - r - g
#         if r + g <= X and g + b <= Y and b + r <= Z:
#             ans += comb(R, r) * comb(G, g) * comb(B, b)
#             ans %= MOD

# print(ans)
