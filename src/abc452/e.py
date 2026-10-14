from math import floor


N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

rui_A = [0 for i in range(N + 1)]
rui_iA = [0 for i in range(N + 1)]
for i in range(N):
    rui_A[i + 1] = (rui_A[i] + A[i]) % MOD
    rui_iA[i + 1] = (rui_iA[i] + A[i] * (i + 1)) % MOD


ans = 0
for j in range(1, M + 1):
    # print("=======", j, "=========")
    # print(f"{N}/{j}:{floor(N / j)}")
    for k in range(1, floor(N / j) + 2):
        # print("k:", k)
        l, r = max(0, j * (k - 1) - 1), min(j * k - 1, N)
        # print(f"{l + 1} -> {r}")
        kia = (rui_iA[r] - rui_iA[l]) % MOD
        ka = (rui_A[r] - rui_A[l]) % MOD
        s = (kia - (ka * (l + 1) if k > 1 else 0)) % MOD
        # print(f"kia: {kia}, ka: {ka}, {l}")
        # print(s, B[j - 1], s * B[j - 1])
        ans = (ans + s * B[j - 1]) % MOD

print(ans)
