N, M = map(int, input().split())
S = list(map(int, input().split()))
imos = [0 for i in range(N + 1)]

for i in range(M):
    L, R, W = map(int, input().split())
    imos[L - 1] += W
    imos[R] -= W

for i in range(N):
    imos[i + 1] += imos[i]


ans = 0
for i in range(N):
    if imos[i] > S[i]:
        ans += 1

print(ans)
