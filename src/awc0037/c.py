N, K = map(int, input().split())
A = list(map(int, input().split()))
A += [0]
MOD = 10**9 + 7

mul = 1

for i in range(K):
    mul = (mul * A[i]) % MOD

ans = 0
for i in range(N - K + 1):
    ans = (ans + mul) % MOD
    mul = (mul * pow(A[i], MOD - 2, MOD)) % MOD
    mul = (mul * A[i + K]) % MOD

print(ans)
