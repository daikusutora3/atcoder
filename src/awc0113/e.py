N, M = map(int, input().split())

K = [list(map(int, input().split())) for i in range(M)]
R = list(map(int, input().split()))

# ある食材に対して食べない人の集合
S = [0 for i in range(N)]
safe = [0 for i in range(N)]
cnt = 0

for i in range(M):
    r = R[i]
    for s in K[i][1:]:
        if r == 0:
            safe[s - 1] = 1
        else:
            S[s - 1] |= 1 << cnt
    if r != 0:
        cnt += 1

f = [0 for i in range(2**cnt)]
mask = 2**cnt - 1
for i, s in enumerate(S):
    if safe[i] == 0:
        f[mask ^ s] += 1

for i in range(cnt):
    for T in range(2**cnt):
        if not ((T >> i) & 1):
            f[T] += f[T ^ (1 << i)]

ans = 0
mod = 998244353
for T in range(2**cnt):
    if T.bit_count() % 2 == 0:
        ans += pow(2, f[T], mod)
    else:
        ans -= pow(2, f[T], mod)
    ans %= mod

print(ans)
