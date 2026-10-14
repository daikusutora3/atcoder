N, W, K = map(int, input().split())

imos = [0 for i in range(N + 1)]
for _ in range(K):
    L = int(input())
    imos[L - 1] += 1
    imos[min(N, L + W - 1)] -= 1

for i in range(N):
    imos[i + 1] += imos[i]


print(*imos[:-1])
