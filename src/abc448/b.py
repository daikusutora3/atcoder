N, M = map(int, input().split())
C = list(map(int, input().split()))

ans = 0
for i in range(N):
    a, b = map(int, input().split())
    ans += min(b, C[a - 1])
    C[a - 1] = max(0, C[a - 1] - b)

print(ans)
