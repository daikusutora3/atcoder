N, R = map(int, input().split())
ans = 0
for _ in range(N):
    X, Y, P, Q = map(int, input().split())
    if (X - P) ** 2 + (Y - Q) ** 2 <= R**2:
        ans += 1

print(ans)
