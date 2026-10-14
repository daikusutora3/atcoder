K = int(input())

ans = 0
mod = 998244353
for a in range(2, K - 3):
    for b in range(2, K - a - 1):
        c = K - a - b
        l = [a, b, c]
        l.sort()
        ans += (l[0] + l[1]) * (l[0] - 1) * (l[1] - 1) * (l[2] - 1)
        ans %= mod

print(ans)
