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


mod = 998244353
fac = Factorial(10**7 + 1, mod)


X1, X2, X3 = map(int, input().split())

ans = 0
for a in range(1, min(X1 + 1, X2 + 2)):
    if X2 - a + X3 >= X3:
        res1 = fac.comb(X2 + 1, a) * fac.comb(X1 - 1, a - 1)
        res3 = fac.comb(X2 - a + X3, X3)
        ans += res1 * res3
        ans %= mod

print(ans)
