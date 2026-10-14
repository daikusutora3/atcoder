from atcoder.string import z_algorithm


def mobius_table(n):
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    comp = bytearray(n + 1)
    for i in range(2, n + 1):
        if not comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            x = i * p
            if x > n:
                break
            comp[x] = 1
            if i % p == 0:
                break
            mu[x] = -mu[i]
    return mu


N = int(input())
S = input()

z = z_algorithm(S)
rz = z_algorithm(S[::-1])

not_del = 0
cnt = [0] * N
for L in range(1, N // 2 + 1):
    # 先頭L文字と末尾L文字が同じ
    same = z[N - L] >= L
    if same:
        for kL in range(2 * L, N + 1, L):
            high = min(kL, L + z[L])
            low = max(0, (kL - (L + rz[L])))
            if kL >= N:
                if high == N and low == 0:
                    not_del = 1
                break
            cnt[kL // L] += max(0, high - low + 1)
    else:
        for kL in range(2 * L, N, L):
            high = min(kL, L + z[L])
            low = max(0, kL - rz[N - L])
            cnt[kL // L] += max(0, high - low + 1)
        for kL in range(2 * L, N, L):
            high = min(kL, z[N - L])
            low = max(0, (kL - (L + rz[L])))
            cnt[kL // L] += max(0, high - low + 1)

mu = mobius_table(N)
ans = not_del
print(ans + sum([-mu[i] * cnt[i] for i in range(2, N)]))
