N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
for p in P:
    ans += p if p % K == 0 else 0

print(ans)
