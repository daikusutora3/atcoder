N, S, C = map(int, input().split())
ans = 0
for _ in range(N):
    h, p = map(int, input().split())
    if h <= S:
        S += -h + p
    else:
        ans += C

print(ans)
