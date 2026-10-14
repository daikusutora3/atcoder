N, T, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
ans = 0
for h in H:
    if h - (H[0] - 1) <= T + K:
        ans += 1

print(ans)
