N, M, K = map(int, input().split())

H = list(map(int, input().split()))
for i in range(N):
    if H[i] < K:
        H[i] = 0

Hr = [0 for i in range(N + 1)]
for i in range(N):
    Hr[i + 1] += H[i] + Hr[i]

ans = 0
for i in range(N):
    ans = max(ans, Hr[min(N, i + M)] - Hr[i])

print(ans)
