N, Q = map(int, input().split())
S = list(map(int, input().split()))

imos = [0 for i in range(N + 1)]

for _ in range(Q):
    l, r = map(int, input().split())
    imos[l - 1] -= 1
    imos[r] += 1

for i in range(N):
    imos[i + 1] += imos[i]

ans = []

for i in range(N):
    ans.append(max(0, S[i] + imos[i]))

print(*ans)
