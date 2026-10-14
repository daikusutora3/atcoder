N, K = map(int, input().split())
data = []
for _ in range(N):
    M = int(input())
    W = set(list(input().split()))
    data.append(W)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if len(data[i] & data[j]) >= K:
            ans += 1

print(ans)
