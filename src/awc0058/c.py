N, M, K = map(int, input().split())

imos = [0 for i in range(N + 1)]

for i in range(M):
    l, r = map(int, input().split())
    imos[l - 1] += 1
    imos[r] -= 1

for i in range(N):
    imos[i + 1] += imos[i]


ans = 0
for i in range(N):
    if imos[i] >= K:
        ans += 1

print(ans)
