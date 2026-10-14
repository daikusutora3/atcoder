N, K = map(int, input().split())
ans = 0
mod = 10**9 + 7
cnt = [0 for i in range(K + 1)]
for g in range(K, 0, -1):
    cnt[g] = pow(K // g, N, mod=mod)
    for i in range(2, K + 1):
        if K < i * g:
            break
        cnt[g] -= cnt[i * g]
        cnt[g] %= mod

ans = 0
for g in range(1, K + 1):
    ans += g * cnt[g]
    ans %= mod

print(ans)
