N, K = map(int, input().split())
mod = 10**9 + 7
S = list(map(int, input().split()))
ans = (sum(S) - max(S) + max(S) * pow(2, K, mod)) % mod

print(ans)
