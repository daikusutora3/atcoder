N, M = map(int, input().split())
S, T = map(int, input().split())
S, T = S - 1, T - 1


# モンハン関数
def P2G(p):
    r = (p) // N
    c = (p) % N
    return [r, c]


if M == 0:
    print(abs(P2G(S)[0] - P2G(T)[0]) + abs(P2G(S)[1] - P2G(T)[1]))
    exit()

P = list(map(int, input().split()))
P = [p - 1 for p in P]

dp = [[float("inf") for __ in range(M)] for _ in range(2**M)]


for i in range(M):
    # Sとiの距離で初期化
    dp[1 << i][i] = abs(P2G(S)[0] - P2G(P[i])[0]) + abs(P2G(S)[1] - P2G(P[i])[1])
for bit in range(0, 2**M):
    for i in range(M):
        for j in range(M):
            # i番目のbitが立っていますか？(もう行ったことがあるから)
            # j番目のbitは立っていないですよね？(今から行くから)
            if (bit >> i & 1) and not (bit >> j & 1):
                # bitの中でj番目を1にする
                dp[bit | 1 << j][j] = min(
                    dp[bit | 1 << j][j],
                    dp[bit][i]
                    + abs(P2G(P[j])[0] - P2G(P[i])[0])
                    + abs(P2G(P[j])[1] - P2G(P[i])[1]),
                )

ans = float("inf")

for i in range(M):
    ans = min(
        ans,
        dp[2**M - 1][i] + abs(P2G(T)[0] - P2G(P[i])[0]) + abs(P2G(T)[1] - P2G(P[i])[1]),
    )

# print(dp)
print(ans)
