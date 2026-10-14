N, K = map(int, input().split())
A = list(map(int, input().split()))
imos = [0 for i in range(N + 1)]

ans = 0
for i in range(N):
    if i < N - K + 1 and (A[i] + imos[i]) % 2 == 1:
        imos[i] += 1
        imos[i + K] -= 1
        ans += 1
    imos[i + 1] += imos[i]

flag = True
for i in range(N):
    if (imos[i] + A[i]) % 2 == 1:
        flag = False

print(ans if flag else -1)
