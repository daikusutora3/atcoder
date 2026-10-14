N, K = map(int, input().split())
T = list(map(int, input().split()))

imos = [0 for i in range(N + 1)]
for i in range(N):
    if i <= N - K:
        if imos[i] < T[i]:
            diff = T[i] - imos[i]
            imos[i] += diff
            imos[i + K] -= diff
    imos[i + 1] += imos[i]

ans = True
for i in range(N):
    if T[i] != imos[i]:
        ans = False

print("Yes" if ans else "No")
