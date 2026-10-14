K = int(input())
rui = [0 for i in range(K + 1)]
MOD = 10**9 + 7
rui[0] = 1
for i in range(K):
    for j in range(max(0, i - 8), i + 1):
        rui[i + 1] = (rui[i + 1] + rui[j]) % MOD

print(rui[K] if K % 9 == 0 else 0)
