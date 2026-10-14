from math import ceil


N, K = map(int, input().split())
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    ans += ceil((a + b) / K)

print(ans)
