N, K = map(int, input().split())
L = list(map(int, input().split()))
mod = 10**9 + 7
ans = (sum(L) - max(L)) % mod

baibai = (max(L) * pow(2, K, mod=mod)) % mod

print((ans + baibai) % mod)
