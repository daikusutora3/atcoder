class Factorial:
    def __init__(self, n, MOD):
        self.fc_list = [1, 1]
        self.fc_inv_list = [1, 1]
        self.inv_list = [1, 1]
        self.MOD = MOD
        for i in range(2, n + 1):
            self.inv_list.append(self.inv_list[MOD % i] * (MOD - MOD // i) % MOD)
            self.fc_inv_list.append(self.fc_inv_list[i - 1] * self.inv_list[i] % MOD)
            self.fc_list.append(self.fc_list[i - 1] * i % MOD)

    def fact(self, n):
        if n >= 0:
            return self.fc_list[n]
        else:
            return self.fc_inv_list[-n]

    def comb(self, n, m):
        MOD = self.MOD
        if n < 0 or m < 0:
            raise Exception("n and m must not be negative")
        if n < m:
            return 0
        return self.fc_list[n] * self.fc_inv_list[m] * self.fc_inv_list[n - m] % MOD

    def perm(self, n, m):
        MOD = self.MOD
        if n < 0 or m < 0:
            raise Exception("n and m must not be negative")
        if n < m:
            return 0
        return self.fc_list[n] * self.fc_inv_list[n - m] % MOD


mod = 10**9 + 7
fac = Factorial(10**6 + 1, mod)


H, W, N = map(int, input().split())
# dp[i][0]: even
# dp[i][1]: odd
dp = [[0, 0] for i in range(N + 2)]
dp[0][0] = 1
rc = [list(map(int, input().split())) for i in range(N)] + [[H, W]]
rc = [[r - 1, c - 1] for r, c in rc]
rc.sort()


for i, (r, c) in enumerate(rc):
    # print(f"{(0, 0)}->{(r, c)}: {fac.comb(r + c, c)}")
    dp[i + 1][1] += (fac.comb(r + c, c)) % mod
    for bi, (br, bc) in enumerate(rc):
        if (not (br <= r and bc <= c)) or i <= bi:
            continue
        w = r - br
        h = c - bc
        # print(f"{(br, bc)}->{(r, c)}: {fac.comb(w + h, h)}")
        dp[i + 1][0] += (dp[bi + 1][1] * fac.comb(w + h, h)) % mod
        dp[i + 1][1] += (dp[bi + 1][0] * fac.comb(w + h, h)) % mod
        dp[i + 1][0] %= mod
        dp[i + 1][1] %= mod

print((dp[-1][1] - dp[-1][0]) % mod)
