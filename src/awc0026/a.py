N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    if (i + 1) % K == 0:
        ans.append(A[i])

print(*ans)
