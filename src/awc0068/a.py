N, L, R = map(int, input().split())

ans = 0
for _ in range(N):
    T = int(input())
    if L <= T <= R:
        ans += 1

print(ans)
