N, K = map(int, input().split())
bt = int(input())
ans = 0
for _ in range(N - 1):
    t = int(input())
    if abs(t - bt) >= K:
        ans += 1
    bt = t

print(ans)
