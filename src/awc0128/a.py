N, K = map(int, input().split())


A = list(map(int, input().split()))

ans = 0
for a in A:
    if a % K == 0:
        ans += 1

print(ans)
