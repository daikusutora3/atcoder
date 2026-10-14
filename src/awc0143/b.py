N, K = map(int, input().split())
P = list(map(int, input().split()))
P.sort(reverse=True)

ans = 0
for i in range(min(N, K)):
    ans += P[i]

print(ans)
