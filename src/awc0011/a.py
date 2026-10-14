N, M = map(int, input().split())
S, T = map(int, input().split())

ans = 0
for _ in range(M):
    p, v = map(int, input().split())
    if S <= p <= T or T <= p <= S:
        ans += v

print(ans)
