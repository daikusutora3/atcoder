N, K = map(int, input().split())
S = list(map(int, input().split()))

K_S = S[K - 1]

ans = 0
for s in S:
    if s < K_S:
        ans += 1

print(ans)
