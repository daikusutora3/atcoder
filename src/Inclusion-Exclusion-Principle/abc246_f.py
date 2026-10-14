N, L = map(int, input().split())
S = [set(input()) for i in range(N)]
mod = 998244353
ans = 0
for bit in range(1, 2**N):
    s = -1
    for i in range(N):
        if bit >> i & 1:
            if s == -1:
                s = S[i].copy()
            else:
                s &= S[i]
    ans += ((-1) ** (bit.bit_count() + 1)) * pow(len(s), L, mod)
    ans %= mod

print(ans)
