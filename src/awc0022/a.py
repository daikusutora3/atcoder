N, D, K = map(int, input().split())
W = list(map(int, input().split()))
ans = 0
for i in range(N):
    if W[i] - D * K >= 1:
        ans += 1

print(ans)
