N, K = map(int, input().split())
ans = 0
for _ in range(N):
    c, d = map(int, input().split())
    ans += d if c <= K else 0

print(ans)
