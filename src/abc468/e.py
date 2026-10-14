mod = 998244353


# xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
def modinv(x):
    global mod
    return pow(x, mod - 2, mod)


N = int(input())
A = list(map(int, input().split()))

rui_mt = [0] * (N + 1)
for i in range(N):
    rui_mt[i + 1] += rui_mt[i] + modinv(i + 1)
    rui_mt[i + 1] %= mod

ans = 0
cnt = 0
i = -1
for i in range(N // 2):
    # print("====")
    # print(f"{N - i}-{i} = {rui_mt[N - i] - rui_mt[i]}")
    cnt += rui_mt[N - i] - rui_mt[i]
    ans += cnt * (A[i] + A[N - 1 - i])
    ans %= mod
    # print(i, N - 1 - i)

i += 1
if N % 2 != 0:
    cnt += modinv(i + 1)
    ans += cnt * A[i]
    ans %= mod

print(ans)
